# Script generated with Bloom
pkgdesc="ROS - roslaunch is a tool for easily launching multiple ROS <a href="http://ros.org/wiki/Nodes">nodes</a> locally and remotely via SSH, as well as setting parameters on the <a href="http://ros.org/wiki/Parameter Server">Parameter Server</a>. It includes options to automatically respawn processes that have already died. roslaunch takes in one or more XML configuration files (with the <tt>.launch</tt> extension) that specify the parameters to set and nodes to launch, as well as the machines that they should be run on."
url='http://ros.org/wiki/roslaunch'

pkgname='ros-lunar-roslaunch'
pkgver='1.13.6_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-lunar-catkin>=0.5.78'
'ros-lunar-rosbuild'
)

depends=('python2-paramiko'
'python2-rospkg>=1.0.37'
'python2-yaml'
'ros-lunar-rosclean'
'ros-lunar-rosgraph-msgs'
'ros-lunar-roslib'
'ros-lunar-rosmaster>=1.11.16'
'ros-lunar-rosout'
'ros-lunar-rosparam'
'ros-lunar-rosunit>=1.13.3'
)

conflicts=()
replaces=()

_dir=roslaunch
source=()
md5sums=()

prepare() {
    cp -R $startdir/roslaunch $srcdir/roslaunch
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/lunar/setup.bash ] && source /opt/ros/lunar/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/lunar \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

