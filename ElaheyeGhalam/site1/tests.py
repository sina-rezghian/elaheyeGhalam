from html.parser import HTMLParser
from urllib.parse import unquote, urlsplit

from django.contrib.staticfiles import finders
from django.test import SimpleTestCase
from django.urls import resolve, reverse


class PageLinks(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        for name, value in attrs:
            if name in ('src', 'href', 'action') and value:
                self.links.append(value)


class WebsiteTests(SimpleTestCase):
    def test_pages_and_all_referenced_local_files_exist(self):
        for name in ('index', 'decorsazi', 'aboutus', 'contactus',
                     'ghorfesazi', 'kabinet_sazi', 'chap_va_tablighat', 'search'):
            with self.subTest(page=name):
                response = self.client.get(reverse(name))
                self.assertEqual(response.status_code, 200)
                self.assertContains(response, 'lang="fa" dir="rtl"')
                parser = PageLinks()
                parser.feed(response.content.decode())
                for link in parser.links:
                    url = urlsplit(link)
                    if url.scheme or url.netloc or not url.path:
                        continue
                    if url.path.startswith('/static/'):
                        asset_path = unquote(url.path[len('/static/'):])
                        self.assertTrue(finders.find(asset_path), msg=link)
                    else:
                        self.assertTrue(url.path.startswith('/'), link)
                        self.assertIsNotNone(resolve(url.path), link)

    def test_search_finds_persian_and_arabic_letter_variants(self):
        for query in ('کابینت', 'كابينت', 'کابینت سازی'):
            with self.subTest(query=query):
                response = self.client.get(reverse('search'), {'q': query})
                self.assertEqual(response.status_code, 200)
                self.assertIn('kabinet_sazi', [result['url'] for result in response.context['results']])

    def test_search_empty_unknown_and_escaped_queries(self):
        for query in ('', 'nonexistent-service', '<script>alert(1)</script>'):
            with self.subTest(query=query):
                response = self.client.get(reverse('search'), {'q': query})
                self.assertEqual(response.status_code, 200)
                self.assertEqual(response.context['results'], [])
                self.assertNotContains(response, '<script>alert(1)</script>')

    def test_contact_links_preserve_original_details(self):
        response = self.client.get(reverse('contactus'))
        for link in ('tel:+982188874158', 'tel:+989046062310',
                     'tel:+989399216613', 'mailto:Elaheghalamparsian@gmail.com'):
            self.assertContains(response, link)
