import logging

import pyramid_sqla as psa
import sqlalchemy as sa
import sqlalchemy.orm as orm
import transaction
import hashlib
import urllib

from pylonshq.lib.sqlalchemy_ext import FromCache, RelationshipCache, CachingQuery
from beaker.cache import cache_region

log = logging.getLogger(__name__)

Base = psa.get_base()
Session = psa.get_session()
Session.configure(extension=[psa._zte], query_cls=CachingQuery)

class BaseModel(object):
    
    @classmethod
    def _get_keys(cls):
        """ return column names for this model """ 
        return orm.class_mapper(cls).c.keys()
    
    def get_dict(self):
        """ return dict with keys and values corresponding to this model data """
        d = {}
        for k in self._get_keys():
            d[k] = getattr(self, k)
        return d
    
    def get_appstruct(self):
        """ return dict with keys and values corresponding to this model data """
        l = []
        for k in self._get_keys():
            l.append((k, getattr(self, k),))
        return l
    
    def populate_obj(self, appstruct):
        """ populate model with data from appstruct """
        for k in self._get_keys():
            if k in appstruct:
                setattr(self, k, appstruct[k])
                
class UserMapperExtension(sa.orm.interfaces.MapperExtension):
    
    def after_update(self, mapper, connection, instance):
        User.by_username(instance.username, invalidate=True)
        
    def after_delete(self, mapper, connection, instance):
        User.by_username(instance.username, invalidate=True)


class User(Base, BaseModel):
    __tablename__ = 'users'
    __mapper_args__ = {'extension': UserMapperExtension()}
    id = sa.Column(sa.Integer(), primary_key=True)
    username = sa.Column(sa.Unicode(30), unique=True)
    password = sa.Column(sa.String(40))
    email = sa.Column(sa.Unicode(100), nullable=False, unique=True)
    status = sa.Column(sa.SmallInteger(), nullable=False)
    firstname = sa.Column(sa.Unicode(25))
    lastname = sa.Column(sa.Unicode(25))
    company_name = sa.Column(sa.Unicode(255), default=u'')         
    last_login_date = sa.Column(sa.TIMESTAMP(timezone=True),
                                default=sa.sql.func.now(),
                                server_default=sa.func.now()
                                )    
    
    def __repr__(self):
        return '<User: %s>' % self.username
    
    groups_dynamic = sa.orm.relationship('Group', secondary='users_groups',
                        lazy='dynamic',
                        passive_deletes=True,
                        passive_updates=True
                        )
    
    user_permissions = sa.orm.relationship('UserPermission',
                        cascade="all, delete-orphan",
                        passive_deletes=True,
                        passive_updates=True
                        )
    
    @property
    def permissions(self):
        q = Session.query(GroupPermission.perm_name.label('perm_name'))
        q = q.filter(GroupPermission.group_name == UserGroup.group_name)
        q = q.filter(User.username == UserGroup.username)
        q = q.filter(User.username == self.username)
        q2 = Session.query(UserPermission.perm_name.label('perm_name'))
        q2 = q2.filter(User.username == self.username)
        q = q.union(q2)
        return [row.perm_name for row in q]
    
    def gravatar_url(self, default='mm'):
        # construct the url
        gravatar_url = "http://www.gravatar.com/avatar/" \
                        + hashlib.md5(self.email.lower()).hexdigest() + "?"
        gravatar_url += urllib.urlencode({'d':default})
        return gravatar_url
    
    @classmethod
    def pass_crypt(cls, text):      
        crypt = hashlib.sha1(text)
        return crypt.hexdigest()
    
    @classmethod
    def by_username(cls, username, cache=FromCache("default_term", "by_id"),
                    invalidate=False):
        q = Session.query(cls).filter(cls.username == username)
        if cache:
            q = q.options(sa.orm.eagerload(User.groups))
            q = q.options(cache)
        if invalidate:
            q.invalidate()
            return True
        return q.first()
    
    @classmethod
    def by_usernames(cls, usernames, cache=FromCache("default_term", "by_id"),
                    invalidate=False):
        q = Session.query(cls).filter(cls.username.in_(usernames))
#        if cache:
#            q = q.options(sa.orm.eagerload(User.groups))
#            q = q.options(cache)
#        if invalidate:
#            q.invalidate()
#            return True
        return q
    
    @classmethod
    def by_email(cls, email, cache=FromCache("default_term", "by_id"),
                    invalidate=False):
        q = Session.query(cls).filter(cls.email == email)
        if cache:
            q = q.options(sa.orm.eagerload(User.groups))
            q = q.options(cache)
        if invalidate:
            q.invalidate()
            return True
        return q.first()


class Group(Base, BaseModel):
    __tablename__ = 'groups'
    group_name = sa.Column(sa.Unicode(50), primary_key=True)
    description = sa.Column(sa.Text())
    member_count = sa.Column(sa.Integer(), nullable=False, default=0)
    
    users = sa.orm.relationship('User',
                        secondary='users_groups',
                        order_by='User.username',
                        passive_deletes=True,
                        passive_updates=True,
                        backref='groups'
                        )
    
    # dynamic property because we may want to cache users relation at later point 
    users_dynamic = sa.orm.relationship('User',
                        secondary='users_groups',
                        order_by='User.username',
                        lazy="dynamic"
                        )
    
    permissions = sa.orm.relationship('GroupPermission',
                        backref='groups',
                        cascade="all, delete-orphan",
                        passive_deletes=True,
                        passive_updates=True
                        )

    
    def __repr__(self):
        return '<Group: %s>' % self.group_name
    
    @classmethod
    def all(cls):
        q = Session.query(Group)
        return q
    
    @classmethod
    def by_group_name(cls, group_name):
        q = Session.query(cls).filter(cls.group_name == group_name)
        return q.first()

    @sa.orm.validates('permissions')
    def validate_permission(self, key, permission):
        assert permission.perm_name in self.__possible_permissions__
        return permission


    def get_user_paginator(self, page=1, item_count=None, items_per_page=50,
                           usernames=None, GET_params={}):
        GET_params.pop('page', None)
        q = self.users_dynamic
        if usernames:
            q = q.filter(UserGroup.username.in_(usernames))
        return webhelpers.paginate.Page(q, page=page,
                                     item_count=item_count,
                                     items_per_page=items_per_page,
                                     sqlalchemy_Session=Session,
                                     **GET_params
                                     )
        
        
class GroupPermission(Base, BaseModel):
    __tablename__ = 'groups_permissions'
    group_name = sa.Column(sa.Unicode(50),
                         sa.ForeignKey('groups.group_name', onupdate='CASCADE',
                                       ondelete='CASCADE'), primary_key=True)
    perm_name = sa.Column(sa.Unicode(30), primary_key=True)
    
    def __repr__(self):
        return '<GroupPermission: %s>' % self.perm_name
    
    @classmethod
    def by_group_and_perm(cls, group_name, perm_name):
        q = Session.query(cls).filter(cls.group_name == group_name)
        q = q.filter(cls.perm_name == perm_name)
        return q.first()
    

class UserPermission(Base, BaseModel):
    __tablename__ = 'users_permissions'
    username = sa.Column(sa.Unicode(50),
                         sa.ForeignKey('users.username', onupdate='CASCADE',
                                       ondelete='CASCADE'), primary_key=True)
    perm_name = sa.Column(sa.Unicode(30), primary_key=True)
    
    def __repr__(self):
        return '<UserPermission: %s>' % self.perm_name
    
    @classmethod
    def by_user_and_perm(cls, username, perm_name):
        q = Session.query(cls).filter(cls.username == username)
        q = q.filter(cls.perm_name == perm_name)
        return q.first()
    
    
class UserGroup(Base, BaseModel):
    __tablename__ = 'users_groups'
    group_name = sa.Column(sa.Unicode(50),
                         sa.ForeignKey('groups.group_name', onupdate='CASCADE',
                                       ondelete='CASCADE'), primary_key=True)

    username = sa.Column(sa.Unicode(30),
                        sa.ForeignKey('users.username', onupdate='CASCADE',
                                      ondelete='CASCADE'), primary_key=True)

    def __repr__(self):
        return '<UserGroup: %s, %s>' % (self.group_name, self.username,)