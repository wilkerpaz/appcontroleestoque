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
        data_update_user = {'name': 'test update', 'username': self.user.username, 'email': 'test@test.com'}
        self.assertEquals(self.user.username, 'test')
        self.client.post(self.url_account_update_user, data_update_user)
        self.user.refresh_from_db()
        self.user = User.objects.get(username='test')
        self.assertEquals(self.user.name, 'test update')

#        self.assertRedirects(response, self.url_account_index)




#     def test_register_error(self):
#         data = {'username': 'test', 'password1': 'test123', 'password2': 'test123'}
#         response = self.client.post(self.url, data)
#         self.assertFormError(response, 'form', 'email', 'Este campo é obrigatório.')
#
#
# class UpdateUserTestCase(TestCase):
#
#     def setUp(self):
#         self.client = Client()
#         self.url_login = reverse('account:login')
#         self.url = reverse('account:update_user')
#         # self.user = mommy.make(User)
#         # self.name = 'Mommy Test'
#         # self.username = 'mommy'
#         # self.email = 'mommy@mommy.com'
#         # self.password1('Salobo@123')
#         # self.password2('Salobo@123')
#
#
#     def test_response(self):
#         response = self.client.get(self.url)
#         self.assertEquals(response.status_code, 302)
#
#     def test1_update_user_ok(self):
#         data = {'name': 'test first', 'email': 'test@test.com'}
#         self.client.login(username='mommy', password='Salobo@123')
#         self.assertEquals(self.user.username, 'mommy')
#         response = self.client.post(self.url, data)
#         url_redirect = reverse('account:login')
#         self.assertRedirects(response, url_redirect)
#         self.assertEquals(response.status_code, 302)
#         self.user.refresh_from_db()
#         user = User.objects.get(username='mommy')
#         self.assertEquals(user.name, 'test first')
#         self.assertEquals(user.email, 'test@test.com')
#
