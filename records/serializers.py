from datetime import datetime
from rest_framework import serializers
from .models import Records
from services.models import Services


def record_time_valid(record_time: datetime) -> bool:
    """Check that 'record_time' is after today."""
    return datetime.now().timestamp() < record_time.timestamp()


def phone_number_valid(phone_number: str) -> bool:
    """Check RU region phone number."""
    pn = phone_number
    return len(pn) == 11 and pn[0] in ['7', '8'] and pn.isdigit() or\
        len(pn) == 12 and pn[:2] == '+7' and pn[1:].isdigit()


class RecordsSerializer(serializers.ModelSerializer):
    def validate(self, data):
        if not phone_number_valid(data['visitors_phone']):
            raise serializers.ValidationError('ERROR: Введите правильный номер телефона')
        if not record_time_valid(data['record_time']):
            raise serializers.ValidationError('ERROR: Укажите верное время записи')
        print(data['service_id'])
        pn = data['visitors_phone']
        data['visitors_phone'] = '+7 ({}) {}-{}-{}'.format(pn[-10:-7], pn[-7:-4], pn[-4:-2], pn[-2:])
        return data

    class Meta:
        model = Records
        fields = "__all__"
