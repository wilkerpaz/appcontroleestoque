from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse
from model_mommy import mommy

User = get_user_model()


class RegisterViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('account:register')

    def test_register_ok(self):
        data = {
            'username': 'test',
            'name': 'Test Fist',
            'email': 'test@test.com',
            'password1': 'test123Ok',
            'password2': 'test123Ok'}
        response = self.client.post(self.url, data)
        index_url = reverse('account:login')
        self.assertEquals(User.objects.count(), 1)
        self.assertRedirects(response, index_url)
        response = self.client.get(index_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='account/login.html')

    def test_register_error(self):
        data = {'username': 'test', 'password1': 'test123', 'password2': 'test123'}
        response = self.client.post(self.url, data)
        self.assertFormError(response, 'form', 'email', 'Este campo é obrigatório.')


class UpdateUserTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.url_login = reverse('account:login')
        self.url = reverse('account:update_user')
        self.user = mommy.make(User)
        self.user.username = 'mommy'
        self.user.set_password('Salobo@123')
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_update_user_ok(self):
        data = {'name': 'test first', 'email': 'test@test.com'}
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 302)
        self.client.login(username='mommy', password='Salobo@123')
        self.assertEquals(self.user.username, 'mommy')
        response = self.client.post(self.url, data)
        url_redirect = reverse('account:login')
        self.assertRedirects(response, url_redirect)
        self.assertEquals(response.status_code, 302)
        self.user.refresh_from_db()
        user = User.objects.get(username='mommy')
        self.assertEquals(user.name, 'test first')
        self.assertEquals(user.email, 'test@test.com')

