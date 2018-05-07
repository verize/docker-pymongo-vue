user_schema = {
    'name': {
        'type': 'string',
        'minlength': 5,
        'maxlength': 25,
        'required': True,
        'unique': True
    },
    'email': {
        'type': 'string',
        'minlength': 8,
        'maxlength': 30,
        'required': True,
        'unique': True
    },
    'password': {
        'type': 'string',
        'minlength': 5,
        'maxlength': 15,
        'required': True,
        'unique': False
    },
    # An embedded 'strongly-typed' dictionary.
    'location': {
        'type': 'dict',
        'schema': {
            'address': {'type': 'string'},
            'city': {'type': 'string'}
        }
    },
    'enabled': {
        'type': 'boolean',
        'default': True
    },
    # 'role' is a list, and can only contain values from 'allowed'.
    'roles': {
        'type': 'list',
        'allowed': ["basic", "admin", "super_admin"],
        'required': True
    },
}

users_resource = {
    'schema': user_schema,
    # We also disable endpoint caching as we don't want client apps to
    # cache account data.
    'cache_control': '',
    'cache_expires': 0,

    # Only allow superusers and admins.
    'allowed_roles': ['superadmin', 'admin'],
    'resource_methods': ['GET', 'POST']
}
