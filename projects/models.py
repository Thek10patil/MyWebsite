from django.db import models


class Projects(models.Model):
    title = models.CharField(max_length=200)
    course_name = models.CharField(max_length=200)
    body = models.TextField()
    year = models.CharField(max_length=200)
    created_at = models.CharField(max_length=200)
    githublink = models.CharField(max_length=200)
    technologyused = models.TextField()
    instructor = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Projects"


class Courses(models.Model):
    course_name = models.CharField(max_length=200)
    created_at = models.CharField(max_length=200)

    def __str__(self):
        return self.course_name

    class Meta:
        verbose_name_plural = "Courses"


class Aboutme(models.Model):
    about = models.TextField()

    def __str__(self):
        return 'Aboutme'

    class Meta:
        verbose_name_plural = "Aboutme"


class Contacts(models.Model):
    contact_details = models.CharField(max_length=200)
    contact_link = models.CharField(max_length=200)

    def __str__(self):
        return self.contact_details

    class Meta:
        verbose_name_plural = "Contacts"
