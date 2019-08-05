source ./venv/bin/activate
export STORE_ORDER_UPDATE_URL="http://127.0.0.1:8020/orders/update/"
export WAREHOUSE_ORDER_CREATE_URL="http://127.0.0.1:8011/orders/create/"

USER="admin"
PASS="super_password"
MAIL="admin@mail.com"
script="
from django.contrib.auth.models import User;

username = '$USER';
password = '$PASS';
email = '$MAIL';

if User.objects.filter(username=username).count()==0:
    User.objects.create_superuser(username, email, password);
    print('Superuser created.');
else:
    print('Superuser creation skipped.');
"
python ./store/manage.py migrate
printf "$script" | python ./store/manage.py shell

python ./warehouse/warehouse/manage.py migrate
printf "$script" | python ./warehouse/warehouse/manage.py shell

supervisord -c supervisord.conf
