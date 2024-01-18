from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from users.models import CustomUser


@api_view(["GET"])
def hello_world(request: Request) -> Response:
    return Response({"message": f"Hello, {request.user}!"})


@api_view(["POST"])
def register_user(request: Request) -> Response:
    try:
        print(request.data)
        user = CustomUser.objects.create_user(
            email=request.data["email"],
            password=request.data["password"],
        )
        return Response({"message": f"User {user} created!"})
    except Exception as e:
        return Response({"message": f"Error creating user: {e}"}, status=400)


@api_view(["POST"])
def set_user_field(request: Request) -> Response:
    try:
        print(request.data)
        user = CustomUser.objects.get(email=request.data["email"])
        setattr(user, request.data["field"], request.data["value"])
        user.save()
        return Response({"message": f"User {user} updated!"})
    except Exception as e:
        return Response({"message": f"Error updating user: {e}"}, status=400)


# TODO: GET User info via serializer Endpoint
