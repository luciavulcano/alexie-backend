from django.apps import apps
from django.db import DEFAULT_DB_ALIAS, connections
from django.core.management.base import BaseCommand, CommandError
from django.db.migrations.recorder import MigrationRecorder
from django.db.migrations.loader import AmbiguityError, MigrationLoader
from django.conf import settings
from os import listdir
import os.path


class Command(BaseCommand):
    help = "Generate SQL file"
    prefix_file = "ALEXIE_RAW_SQL"
    default_path = f"{settings.BASE_DIR}/sql"
    output_transaction = False

    def check_query_exists(self):

        merged_already_exists = ""
        files_count = 0

        for file_name in listdir(self.default_path):

            if self.prefix_file not in file_name:
                continue
            full_path = f"{self.default_path}/{file_name}"
            files_count += 1

            with open(full_path, "r+") as file:
                for line in file.readlines():
                    merged_already_exists += line

        return files_count, merged_already_exists

    def generate_file(self, raw_sql, files_count=0):

        actual_count = files_count + 1
        file_name = f"{self.prefix_file}_{str(actual_count).zfill(3)}.sql"

        full_path = f"{self.default_path}/{file_name}"

        with open(full_path, "w+") as file:
            file.write(raw_sql)
            file.close()

        return file_name

    def check_folder(self):
        if not os.path.isdir(self.default_path):
            os.mkdir(self.default_path)

    def handle(self, *args, **options):
        # Get the database we're operating from
        connection = connections[DEFAULT_DB_ALIAS]
        raw_sql = "BEGIN;\n"
        new_query_found = False

        self.check_folder()

        files_count, merged_already_exists = self.check_query_exists()

        # Load up a loader to get all the migration data, but don't replace
        # migrations.
        loader = MigrationLoader(connection, replace_migrations=False)

        # Resolve command-line arguments into a migration
        migrations = MigrationRecorder.Migration.objects.all()
        for migration in migrations:
            app_label, migration_name = migration.app, migration.name
            # Validate app_label
            try:
                apps.get_app_config(app_label)
            except LookupError as err:
                raise CommandError(str(err))
            if app_label not in loader.migrated_apps:
                raise CommandError("App '%s' does not have migrations" % app_label)
            try:
                migration = loader.get_migration_by_prefix(app_label, migration_name)
            except AmbiguityError:
                raise CommandError(
                    "More than one migration matches '%s' in app '%s'. Please be more "
                    "specific." % (migration_name, app_label)
                )
            except KeyError:
                raise CommandError(
                    "Cannot find a migration matching '%s' from app '%s'. Is it in "
                    "INSTALLED_APPS?" % (migration_name, app_label)
                )
            target = (app_label, migration.name)

            # Make a plan that represents just the requested migrations and show SQL
            # for it

            plan = [(loader.graph.nodes[target], False)]
            sql_statements = loader.collect_sql(plan)

            if not sql_statements:
                continue

            actual_sql = "\n".join(sql_statements)

            if actual_sql not in merged_already_exists:
                raw_sql += "\n".join(sql_statements)
                new_query_found = True

        raw_sql += "\nCOMMIT;"

        if new_query_found:
            new_file_name = self.generate_file(raw_sql=raw_sql, files_count=files_count)
            return f"New sql file generated with name: {new_file_name}"

        return "Process Finished.\nNo modifications found!"
