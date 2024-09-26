# Generated by Django 1.9.11 on 2016-11-11 17:04
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("wagtailimages", "0015_fill_filter_spec_field"),
    ]

    operations = [
        migrations.AlterField(
            model_name="rendition",
            name="filter_spec",
            field=models.CharField(db_index=True, max_length=255),
        ),
        # New step introduced in Wagtail 1.8.1:
        #
        # Reduce max_length of rendition.focal_point_key to 16, from the previous value of 255
        # which existed on Wagtail <= 1.8. MySQL has a limit of 767 (on InnoDB) or 1000 (on MyISAM)
        # bytes; depending on the character encoding used, this limit may be reached by the
        # original index on ['image', 'filter', 'focal_point_key'] (= 1 varchar and two FKs)
        # or the new index on ['image', 'filter_spec', 'focal_point_key'] (= 2 varchars and one FK).
        #
        # To mitigate this, we reduce focal_point_key in the following places:
        # * Retrospectively in the original migration, so that configurations that previously
        #   failed on wagtailimages/0001_initial can now run (see #2925 / #2953);
        # * Here, so that previously-working Wagtail <=1.7 installations that failed on the
        #   AlterUniqueTogether below when upgrading to 1.8 can now succeed;
        # * In the newly-added migration wagtailimages/0017, so that existing Wagtail 1.8 installations
        #   that successfully applied the old 1.8 version of this migration are consistent with
        #   other setups.
        #
        # Since Django will optimise away any AlterField operations that appear to match
        # the current state (according to earlier migrations) - which would cause them to be
        # skipped on installations that ran the earlier (max_length=255) versions of the
        # migrations - we need to make them superficially different; we do this by stepping
        # max_length down from 18 to 17 then 16.
        #
        # Projects with a custom image model don't have to worry about this - they'll have an existing
        # migration with the max_length=255, and will get a new migration reducing it to max_length=16
        # the next time they run makemigrations.
        migrations.AlterField(
            model_name="rendition",
            name="focal_point_key",
            field=models.CharField(
                blank=True, default="", max_length=17, editable=False
            ),
        ),
        migrations.AlterUniqueTogether(
            name="rendition",
            unique_together={("image", "filter_spec", "focal_point_key")},
        ),
    ]
