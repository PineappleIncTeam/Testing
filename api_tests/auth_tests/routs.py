
auth_api_routes = {
    'auth': {
        'post_login': '/api/v1/auth/token/login',
        'post_logout': '/api/v1/auth/token/logout',
        'get_users': '/api/v1/auth/users',
        'post_users': '/api/v1/auth/users',
        'get_users_id': '/api/v1/auth/users/{}',
        'put_users_id': '/api/v1/auth/users/{}',
        'patch_users_id': '/api/v1/auth/users/{}',
        'get_users_me': '/api/v1/auth/users/me',
        'put_users_me': '/api/v1/auth/users/me',
        'patch_users_me': '/api/v1/auth/users/me',
        'delete_users_me': '/api/v1/auth/users/me',
        'post_users_resend_activation': 'api/v1/auth/users/resend_activation',
        'post_users_reset_emai': 'api/v1/auth/users/reset_email',
        'post_users_reset_email_confirm': 'api/v1/auth/users/reset_email_confirm',
        'post_users_reset_password': 'api/v1/auth/users/reset_password',
        'post_users_set_email': 'api/v1/auth/users/set_email',
        'post_users_set_password': 'api/v1/auth/users/set_password'
    }
}