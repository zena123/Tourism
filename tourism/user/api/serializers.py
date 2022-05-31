from django.contrib.auth import get_user_model, login
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from rest_framework.validators import UniqueValidator

from ..models import Profile

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "name", "url"]

        extra_kwargs = {
            "url": {"view_name": "user_api:user-detail", "lookup_field": "username"}
        }


class ProfileSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(
        required=True,
        label=_("first name"),
        style={
            "placeholder": _("Enter your first name"),
        },
    )
    last_name = serializers.CharField(
        required=True,
        label=_("last name"),
        style={
            "placeholder": _("Enter your last name"),
        },
    )
    username = serializers.CharField(
        required=True,
        label=_("Username"),
        validators=[UniqueValidator(queryset=User.objects.all())],
        style={
            "placeholder": _("Add username"),
        },
    )
    email = serializers.EmailField(
        required=True,
        label=_("Email"),
        validators=[UniqueValidator(queryset=User.objects.all())],
    )
    password = serializers.CharField(
        write_only=True,
        style={"input_type": "password", "rules": "required|min:8"},
    )
    repeat_password = serializers.CharField(
        label=_("Confirm password"),
        write_only=True,
        style={
            "input_type": "password",
            "rules": "confirmed:password|required|min:8",
        },
    )

    class Meta:
        model = Profile
        fields = "__all__"

    def validate(self, attrs):
        password = attrs.get("password", None)
        repeat_password = attrs.pop("repeat_password", None)
        if password and repeat_password and password != repeat_password:
            raise serializers.ValidationError(
                {"repeat_password": _("Passwords Do not Match")}
            )
        return attrs

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User.objects.create(
            username=validated_data["username"],
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
        )
        user.set_password(password)
        user.save()
        login(
            self.context["request"],
            user,
            backend="django.contrib.auth.backends.ModelBackend",
        )
        validated_data["user"] = user
        return super(ProfileSerializer, self).create(validated_data)

