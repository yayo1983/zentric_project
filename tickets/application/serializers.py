from rest_framework import serializers
from tickets.infrastructure.models import Ticket

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['id', 'title', 'description', 'created_at', 'updated_at', 'status', 'assigned_to']
        read_only_fields = ['created_at', 'updated_at']

    def validate_status(self, value):
        if value not in ['open', 'in_progress', 'closed']:
            raise serializers.ValidationError("Estado inválido.")
        return value
