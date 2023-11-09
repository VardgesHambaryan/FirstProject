from django.db import models

class Blog(models.Model):
    img = models.ImageField('Image' , upload_to='media')
    title = models.CharField('Title' , max_length=255)
    text = models.TextField('Text')
    date = models.DateField('Date')

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Blog Post'
        verbose_name_plural = 'Blog Posts'


class HomeBG(models.Model):
    image1 = models.ImageField("First Background Image", upload_to="media")
    image2 = models.ImageField("Second Background Image", upload_to="media")
    image3 = models.ImageField("Third Background Image", upload_to="media")
    image4 = models.ImageField("Forth Background Image", upload_to="media")

    def __str__(self) -> str:
        return 'Home Backgroud'
    
    class Meta:
        verbose_name = "Home Background"
        verbose_name_plural = "Home Backgrounds"

class OurService(models.Model):
    text1 = models.TextField('First Text')
    text2 = models.TextField('Second Text')

    def __str__(self) -> str:
        return 'OurService'
    
    class Meta:
        verbose_name = 'Our Service'
        verbose_name_plural = 'Our Services'


class OurGallery(models.Model):

    title = models.CharField('Title' , max_length=50)
    subtitle = models.CharField('SubTitle' , max_length=50)
    img_small = models.ImageField('Small Image' , upload_to='media')
    img_large = models.ImageField('Large Image' , upload_to='media')

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Our Gallery'
        verbose_name_plural = 'Our Galleries'


class ContactUs(models.Model):

    name = models.CharField('Name' , max_length=50)
    email = models.EmailField('Email' , null=True)
    message = models.TextField('Message')

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Contact Us'
        verbose_name_plural = 'Contact Us'


class AboutUS(models.Model):
    text1 = models.TextField('text1')
    text2 = models.TextField('text2')
    text3 = models.TextField('text3')

    def __str__(self) -> str:
        return 'About Us'
    
    class Meta:
        verbose_name = 'About Us'
        verbose_name_plural = 'About Us'
        
    

class Icons(models.Model):
    icon = models.CharField('icon', max_length=100)
    text = models.TextField('text')

    def __str__(self) -> str:
        return self.icon
    

    class Meta:
        verbose_name = 'Icon'
        verbose_name_plural = 'Icons'


