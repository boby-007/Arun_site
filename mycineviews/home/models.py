from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.fields import StreamField
from wagtail import blocks
from wagtail.admin.panels import FieldPanel
from wagtail.images.blocks import ImageChooserBlock


# Create your models here.
from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField,StreamField
from wagtail.admin.panels import FieldPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail import blocks

# Create your models here.
class BlogIndexPage(Page):
    heading=models.CharField(max_length=250)
    intro = RichTextField(blank=True)



    content_panels = Page.content_panels + [
        FieldPanel('heading', classname="full"),
        FieldPanel('intro', classname="full")
    ]

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        blogpages= BlogDetailPage.objects.all().order_by('-first_published_at')
        context['blogpages'] = blogpages
        return context 

class BlogDetailPage(Page):
    short_heading=models.CharField(max_length=100,blank=True)
    date = models.DateField("Post date")
    body = StreamField([
        ('heading', blocks.CharBlock(form_classname="full title")),
        ('blog', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
    ], use_json_field=True)
    description=RichTextField(blank=True)
    blog_template = models.ForeignKey('wagtailimages.Image', null=True, blank=True,on_delete=models.SET_NULL, related_name='+'
    )


    content_panels = Page.content_panels + [
        FieldPanel('short_heading'),
        FieldPanel('date'),
        FieldPanel('body'),
        FieldPanel('description'),
        FieldPanel('blog_template')
        
    ]

    class Meta:
        ordering = ['date']