# Script that sets up your web servers for the deployment of web_static

exec {'update':
  provider => shell,
  command  => 'sudo apt-get -y update',
  before   => Exec['install Nginx'],
}

exec {'install Nginx':
  provider => shell,
  command  => 'sudo apt-get -y install nginx',
  before   => Exec['start Nginx'],
}

exec {'start Nginx':
  provider => shell,
  command  => 'sudo service nginx start',
  before   => Exec['create directory 01'],
}

exec {'create directory 01':
  provider => shell,
  command  => 'sudo mkdir -p /data/web_static/releases/test/',
  before   => Exec['create directory 02'],
}

exec {'create directory 02':
  provider => shell,
  command  => 'sudo mkdir -p /data/web_static/shared/',
  before   => Exec['dummy content into html'],
}

exec {'dummy content into html':
  provider => shell,
  command  => 'echo "Test content" | sudo tee /data/web_static/releases/test/index.html',
  before   => Exec['symbolic link'],
}

exec {'create symbolic link':
  provider => shell,
  command  => 'sudo ln -sf /data/web_static/releases/test/ /data/web_static/current',
  before   => Exec['edit nginx conf location block'],
}

exec {'edit nginx conf location block':
  provider => shell,
  command  => 'sudo sed -i \'38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current//hbnb_static/;\n\t\tautoindex off;\n\t}\n\' /etc/nginx/sites-available/default',
  before   => Exec['restart Nginx'],
}

exec {'restart Nginx':
  provider => shell,
  command  => 'sudo service nginx restart',
  before   => File['/data/']
}

file {'/data/':
  ensure  => directory,
  owner   => 'ubuntu',
  group   => 'ubuntu',
  recurse => true,
}
