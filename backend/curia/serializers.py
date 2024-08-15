from rest_framework import serializers
from .models import Announcement, Curia


class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Announcement
        fields = [
            'curia', 
            'date', 
            'title', 
            'body', 
            'image'
        ]


class CuriaSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Curia
        fields = [
            'name', 
            'state', 
            'country', 
            'parish',
            'spiritual_director'
        ]

#    name = models.CharField(max_length=100)
#     state = models.CharField(max_length=100)
#     country = models.CharField(max_length=50, default="Nigeria")
#     parish = models.CharField(max_length=100)
#     spiritual_director 

    # owner = UserPublicSerializer(source='user', read_only=True)
    # my_discount = serializers.SerializerMethodField(read_only=True)
    # edit_url = serializers.SerializerMethodField(read_only=True) 
    # url = serializers.HyperlinkedIdentityField(
    #     view_name='product-detail', 
    #     lookup_field='pk'
    #     )
    # title = serializers.CharField(validators=[
    #     validators.validate_title, 
    #     validators.validate_title_no_hello, 
    #     validators.unique_product_title
    # ])
    # email = serializers.EmailField(write_only=True)

    # class Meta: 
    #     model = Curia 
    #     fields = [
    #         'owner',
    #         'url',
    #         'edit_url', 
    #         'pk',
    #         'title', 
    #         'content', 
    #         'price', 
    #         'sale_price', 
    #         'my_discount'
    #     ]



    # def get_edit_url(self, obj): 
    #     request = self.context.get('request')
    #     if request is None:
    #         return None
    #     return reverse("product-edit-detail", kwargs={'pk': obj.pk}, request=request)

    # def get_my_discount(self, obj):
    #     if not hasattr(obj, 'id'):
    #         return None 
    #     if not isinstance(obj, Product):
    #         return None 
    #     return obj.get_discount()