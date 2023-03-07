import datetime
from rest_framework import serializers
from .models import *


class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'


def record_time_valid(record_time: datetime) -> bool:
    """Check that 'record_time' is after today."""
    return datetime.datetime.now().timestamp() < record_time.timestamp()


def phone_number_valid(phone_number: str) -> bool:
    """Check RU region phone number."""
    pn = phone_number
    return len(pn) == 11 and pn[0] in ['7', '8'] and pn.isdigit() or\
        len(pn) == 12 and pn[:2] == '+7' and pn[1:].isdigit()


class RecordSerializer(serializers.ModelSerializer):
    def validate(self, data):
        if not phone_number_valid(data['visitors_phone']):
            raise serializers.ValidationError('ERROR: Введите правильный номер телефона')
        if not record_time_valid(data['record_time']):
            raise serializers.ValidationError('ERROR: Укажите верное время записи')
        pn = data['visitors_phone']
        data['visitors_phone'] = '+7 ({}) {}-{}-{}'.format(pn[-10:-7], pn[-7:-4], pn[-4:-2], pn[-2:])
        return data

    class Meta:
        model = Record
        fields = "__all__"










































# class ServiceModel:
#     def __init__(self, title, duration, price):
#         self.title = title
#         self.duration = duration
#         self.price = price == True

# class ServicesSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=50)
#     description = models.CharField(max_length=255)
#     price = serializers.DecimalField(max_digits=8, decimal_places=2)

    # def create(self, validated_data):
    #     return Services.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.duration = validated_data.get('duration', instance.duration)
    #     instance.price = validated_data.get('price', instance.price)
    #     instance.save()
    #     return instance

# def encode():
#     model = ServiceModel('Первичный осмотр', 15, 699.99)
#     model_sr = ServiceSerializer(model)
#     print(model_sr.data, type(model_sr.data))
#     json = JSONRenderer().render(model_sr.data)
#     print(json)

    # def create(self, validated_data):
    #     timeslot = str(validated_data['record_time'])
    #     if is_valid_record_time(timeslot):
    #         slot = TimeSlot.objects.get(slot=timeslot)
    #         slot.slot_status = False
    #         slot.save()
    #         return Record.objects.create(**validated_data)
    #     raise serializers.ValidationError('ERROR: Время занято')
    #
    # def update(self, instance, validated_data):
    #     old_time_id = Record.objects.get(record_time=instance.record_time).record_time_id
    #     new_time = str(validated_data.get('record_time', instance.record_time))
    #     if not is_valid_record_time(new_time):
    #         raise serializers.ValidationError('ERROR: Время занято')
    #     instance.service = validated_data.get('service', instance.service)
    #     instance.record_time = validated_data.get('record_time', instance.record_time)
    #     instance.visitors_name = validated_data.get('visitors_name', instance.visitors_name)
    #     instance.visitors_email = validated_data.get('visitors_email', instance.visitors_email)
    #     instance.visitors_phone = validated_data.get('visitors_phone', instance.visitors_phone)
    #     slot = TimeSlot.objects.get(slot=new_time)
    #     slot.slot_status = False
    #     slot.save()
    #     slot = TimeSlot.objects.get(pk=old_time_id)
    #     slot.slot_status = True
    #     slot.save()
    #     instance.save()
    #     return instance