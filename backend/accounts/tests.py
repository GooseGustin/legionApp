from django.test import TestCase
from .models import Legionary, User
from curia.models import Curia 

# Create your tests here.
class AccountsTestCase(TestCase):

    def test_create_legionary(self):
        user = User.objects.create_user(
            username='Gamer', password='passG#me123'
        )
        leg1 = Legionary.objects.create(
            user=user, 
            status='non-manager',
        )
        all_legionaries = Legionary.objects.all()
        self.assertIsNotNone(all_legionaries.exists())
        self.assertEqual(leg1.user.username, 'Gamer')
        self.assertEqual(leg1.status, 'non-manager')
    
    def test_become_manager(self):
        user = User.objects.create_user(
            username='Gamer', password='passG#me123'
        )
        leg = Legionary.objects.create(
            user=user, 
            status='non-manager',
        )
        curia = Curia.objects.create(
            name='Our Lady Queen of Mercy', 
            state='Plateau', 
            parish="St. Gabriel's", 
            spiritual_director="Fr. Gabriel"
        )
        leg.curia_managed = curia
        self.assertIsNotNone(leg.curia_managed)

    # name = models.CharField(max_length=100)
    # state = models.CharField(max_length=100)
    # country = models.CharField(max_length=50, default="Nigeria")
    # parish = models.CharField(max_length=100)
    # spiritual_director = models.CharField(max_length=100)
