# -*- coding: utf-8 -*-

# This file is part of wger Workout Manager.
#
# wger Workout Manager is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# wger Workout Manager is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache

from wger.nutrition.models import NutritionPlan, Meal, MealItem
from wger.utils.cache import cache_mapper


# receive signals from the three models
# and delete the nutrition info dictionary from
# cache using current user's primary key when current
# user creates or updates or deletes a nutrition plan
# or a meal or a meal item

@receiver(post_save, sender=NutritionPlan)
@receiver(post_delete, sender=NutritionPlan)
@receiver(post_save, sender=Meal)
@receiver(post_delete, sender=Meal)
@receiver(post_save, sender=MealItem)
@receiver(post_delete, sender=MealItem)
def delete_nutrition_info_from_cache(sender, **kwargs):
    '''
    Delete the nutrition info dict from cache
    '''
    sender_instance = kwargs['instance']

    if sender is NutritionPlan:
        primary_key = sender_instance.pk

    elif sender is Meal:
        primary_key = sender_instance.plan.pk

    else:
        primary_key = sender_instance.meal.plan.pk


    cache.delete(cache_mapper.get_nutritional_info(primary_key))





