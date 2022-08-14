from django.db import models


# Create your models here.

class Attribute(models.Model):
    name = models.CharField(max_length=30)
    value = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Node(models.Model):
    complete = models.CharField(max_length=200)
    label = models.CharField(max_length=100)
    attributes = models.ManyToManyField(Attribute)

    def __str__(self):
        return self.label


class Link(models.Model):
    label = models.CharField(max_length=120)
    parent_node = models.ForeignKey(Node, on_delete=models.CASCADE, related_name='parent_node', default="")
    child_node = models.ForeignKey(Node, on_delete=models.CASCADE, related_name='child_node', default="")

    def __str__(self):
        return self.label