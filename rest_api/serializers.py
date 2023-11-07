from rest_framework.serializers import ( 
  ModelSerializer, 
  HyperlinkedRelatedField, 
  PrimaryKeyRelatedField,
)


from reserva.models import ReservaDeBanho, Petshop
from base.models import Contato


class PetshopModelSerializer(ModelSerializer):
  reservas = HyperlinkedRelatedField(
    many=True,
    read_only=True,
    view_name='api:reserva-detail'
  )

  class Meta:
    model = Petshop
    fields = '__all__'

class PetshopNestedModelSerializer(ModelSerializer):
  class Meta:
    model = Petshop
    fields = '__all__'


class PetshopRelatedFieldCustomSerializer(PrimaryKeyRelatedField):
  def __init__(self, **kwargs):
    self.serializer = PetshopNestedModelSerializer
    super().__init__(**kwargs)

class AgendamentoModelSerializer(ModelSerializer):
  petshop_id = PetshopRelatedFieldCustomSerializer(
    queryset=Petshop.objects.all(),
    read_only=False
  )

  class Meta:
    model = ReservaDeBanho
    fields = '__all__'

class ContatoModelSerializer(ModelSerializer):
  class Meta:
    model = Contato
    fields = '__all__'

  def use_pk_only_optimization(self):
    return False
  
  def to_representation(self, value):
    return self.serializer(value, context=self.context).data