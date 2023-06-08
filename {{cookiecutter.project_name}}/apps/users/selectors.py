from models import CustomUser


def all_users():
    """
    Retrieve all users.

    This function returns a queryset containing all user objects in the system.

    Returns:
        QuerySet: A queryset containing all user objects.

    Example usage:
        To retrieve all users, simply call the function:

        ```python
        users = all_users()
        for user in users:
            print(user.username)
        ```
    """

    return CustomUser.objects.all()
