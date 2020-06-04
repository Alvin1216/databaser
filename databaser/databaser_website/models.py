# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Condition(models.Model):
    condition_occurrence_id = models.IntegerField(primary_key=True, blank=True)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    condition_name = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'condition'


class ConditionPerson(models.Model):
    person = models.ForeignKey('Person', models.DO_NOTHING, blank=True)
    condition_occurrence = models.ForeignKey(Condition, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'condition_person'


class CovidStatus(models.Model):
    person = models.ForeignKey('Person', models.DO_NOTHING, primary_key=True, blank=True)
    status = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'covid_status'


class Drug(models.Model):
    drug_exposure_id = models.IntegerField(primary_key=True, blank=True)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    drug_name = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'drug'


class DrugPerson(models.Model):
    person = models.ForeignKey('Person', models.DO_NOTHING, blank=True, null=True)
    drug_exposure = models.ForeignKey(Drug, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'drug_person'


class Location(models.Model):
    location_id = models.IntegerField(primary_key=True, blank=True)
    country = models.TextField(blank=True, null=True)  # This field type is a guess.
    city = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'location'


class Measurement(models.Model):
    measurement_id = models.IntegerField(primary_key=True, blank=True)
    measurement_date = models.DateTimeField(blank=True, null=True)
    measurement_name = models.TextField(blank=True, null=True)  # This field type is a guess.
    value_as_number = models.TextField(blank=True, null=True)  # This field type is a guess.
    unit_concept_id = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'measurement'


class MeasurementPerson(models.Model):
    person = models.ForeignKey('Person', models.DO_NOTHING, blank=True, null=True)
    measurement = models.ForeignKey(Measurement, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'measurement_person'


class Person(models.Model):
    person_id = models.IntegerField(primary_key=True, blank=True)
    birth_datetime = models.DateTimeField(blank=True, null=True)
    gender = models.TextField(blank=True, null=True)  # This field type is a guess.
    race = models.TextField(blank=True, null=True)  # This field type is a guess.
    age = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'person'


class PersonLocation(models.Model):
    person = models.ForeignKey(Person, models.DO_NOTHING, primary_key=True, blank=True)
    location = models.ForeignKey(Location, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'person_location'
