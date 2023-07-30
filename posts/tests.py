from django.test import TestCase, Client
from django.urls import reverse

from posts.models import Post


class PostsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.post = Post.objects.create(title="Test", content="Test")


    def test_index_view(self):
        response = self.client.get(reverse("index-bek"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("posts/index.html")


    def test_contacts_view(self):
        response = self.client.get(reverse("contacts"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("posts/contacts.html")


    def test_about_view(self):
        response = self.client.get(reverse("about"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("posts/about.html")


    def test_post_update(self):
        response = self.client.get(reverse("post-update", args=(self.post.pk,)))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("posts/post_update.html")


    def test_post_delete(self):
        response = self.client.get(reverse("post-delete", args=(self.post.pk,)))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("posts/post_delete.html")

    
    def test_post_detail(self):
        response = self.client.get(reverse("post-detail", args=(self.post.pk,)))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("posts/post_detail.html")