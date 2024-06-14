from rest_framework import serializers

from core.models import GrantGoal

class ListGrantGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrantGoal
        fields = [
            'ggname',
            'description',
            'user',
            'timestamp',
            'days_duration',
            'state',            
            'status',
        ]

class DetailGrantGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrantGoal
        fields = "__all__"

class CreateGrantGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrantGoal
        fields = "__all__"

class UpdateGrantGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrantGoal
        fields = [
            'ggname',
            'description',
            "days_duration",
            'priority',            
            'status',
            'slug',
        ]