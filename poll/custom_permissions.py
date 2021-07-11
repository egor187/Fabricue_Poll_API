from rest_framework import permissions


class IsAnswerOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow author of an answer to edit it.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:  # for GET, HEAD or OPTIONS requests 'read' is granted
            return True
        return obj.user == request.user  # for all other (POST, PUT) requests granted only for user, who created object


class IsAnswerOwner(permissions.BasePermission):
    """
    Custom permission to only allow author of an answer to edit it.
    """
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user  # for all methods requests granted only for user, who created object
