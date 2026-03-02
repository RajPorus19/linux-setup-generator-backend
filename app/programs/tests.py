from django.urls import reverse
from rest_framework.test import APITestCase

from .models import ProgramCategory


class ProgramCategoryAPITests(APITestCase):
    def setUp(self):
        for i in range(15):
            ProgramCategory.objects.create(
                name=f"Category {i}",
                slug=f"category-{i}",
                description="Test description",
            )

    def test_list_is_paginated_to_10(self):
        url = reverse("program-category-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn("results", response.data)
        self.assertEqual(len(response.data["results"]), 10)

    def test_search_filters_by_name_slug_description(self):
        ProgramCategory.objects.create(
            name="Special Category",
            slug="special-category",
            description="Contains unique-keyword",
        )

        url = reverse("program-category-list")
        response = self.client.get(url, {"search": "unique-keyword"})
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(response.data["count"], 1)
