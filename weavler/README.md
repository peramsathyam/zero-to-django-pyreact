# Migrations

Migrations are Django’s way of propagating changes you make to your models (adding a field, deleting a model, etc.) into your database schema. They’re designed to be mostly automatic, but you’ll need to know when to make migrations, when to run them, and the common problems you might run into.

## The Commands

There are several commands which you will use to interact with migrations and Django’s handling of database schema:

- `migrate`, which is responsible for applying migrations, as well as unapplying and listing their status.
- `makemigrations`, which is responsible for creating new migrations based on the changes you have made to your models.
- `sqlmigrate`, which displays the SQL statements for a migration.
- `showmigrations`, which lists a project’s migrations.

You should think of migrations as a version control system for your database schema. `makemigrations` is responsible for packaging up your model changes into individual migration files - analogous to commits - and `migrate` is responsible for applying those to your database.

The migration files for each app live in a “migrations” directory inside of that app, and are designed to be committed to, and distributed as part of, its codebase. You should be making them once on your development machine and then running the same migrations on your colleagues’ machines, your staging machines, and eventually your production machines.

## Workflow

Make changes to your models - say, add a field and remove a model - and then run `makemigrations`:

```sh
$ python manage.py makemigrations
```

or

If you want to give the migration(s) a meaningful name instead of a generated one, you can use the makemigrations --name option:

    $ python manage.py makemigrations --name changed_my_model your_app_label

Once you have your new migration files, you should apply them to your database to make sure they work as expected:

    $ python manage.py migrate

**ProTip** : limit models migrations to application scope. Avoid cross references between two models in different applications.
