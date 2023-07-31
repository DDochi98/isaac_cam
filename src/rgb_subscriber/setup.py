from setuptools import setup

package_name = 'rgb_subscriber'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='imleb',
    maintainer_email='imleb@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
		'rgb_subscriber_node = rgb_subscriber.display_rgb:main',
		'depth_subscriber_node = rgb_subscriber.display_depth:main',
        ],
    },
)
