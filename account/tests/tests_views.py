from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

User = get_user_model()


class RegisterViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.url_account_register = reverse('account:register')
        self.url_account_index = reverse('account:index')
        self.url_account_logout = reverse('account:logout')
        self.url_account_update_user = reverse('account:update_user')
        self.url_account_update_password = reverse('account:update_password')

        data_register = {
            'username': 'test',
            'name': 'Test Fist',
            'email': 'test@test.com',
            'password1': 'test123Ok',
            'password2': 'test123Ok'}
        self.response = self.client.post(self.url_account_register, data_register)
        self.url_account_login = reverse('account:login')

        self.response_login = self.client.login(username='test', password='test123Ok')

        self.user = User.objects.get(username='test')

    def tearDown(self):
        self.user.delete()

    def test_register_redirect(self):
        self.assertEquals(User.objects.count(), 1)
        self.assertRedirects(self.response, self.url_account_login)

    def test_page_register(self):

        response = self.client.get(self.url_account_register)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='account/register.html')

    def test_login(self):
        self.assertTrue(self.response_login)

    def test_page_login(self):
        response = self.client.get(self.url_account_login)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='account/login.html')

    def test_redirect_logout(self):
        response = self.client.get(self.url_account_logout)
        self.assertRedirects(response, '/')

    def test_redirect_index(self):
        self.client.get(self.url_account_logout)
        response = self.client.get(self.url_account_index)
        self.assertRedirects(response, self.url_account_login+'?next='+self.url_account_index)

    def test_redirect_update_user(self):
        self.client.get(self.url_account_logout)
        response = self.client.get(self.url_account_update_user)
        self.assertRedirects(response, self.url_account_login+'?next='+self.url_account_update_user)

    def test_redirect_update_password(self):
        self.client.get(self.url_account_logout)
        response = self.client.get(self.url_account_update_password)
        self.assertRedirects(response, self.url_account_login+'?next='+self.url_account_update_password)

    def test_page_index(self):
        response = self.client.get(self.url_account_index)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='account/account.html')

    def test_user_creation(self):
        self.assertTrue(User.objects.exists())

    def test_page_update_user(self):
        response = self.client.get(self.url_account_update_user)
        self.assertEquals(response.status_code, 200)

    def test_update_user(self):
        data_update_user = {'name': 'test update', 'username': 'test_update', 'email': 'test_update@test.com'}
        response = self.client.post(self.url_account_update_user, data_update_user)
        self.assertRedirects(response, self.url_account_index)

        self.user.refresh_from_db()
        self.assertEquals(self.user.name, 'test update')
        self.assertEquals(self.user.username, 'test_update')
        self.assertEquals(self.user.email, 'test_update@test.com')

    def test_update_password(self):

        data_update_password = {
            'old_password': 'test123Ok',
            'new_password1': 'Salobo@1234',
            'new_password2': 'Salobo@1234'}
        old_password = self.user.password
        self.client.post(self.url_account_update_password, data_update_password)
        self.user.refresh_from_db()
        new_password = self.user.password
        self.assertNotEquals(old_password, new_password)
