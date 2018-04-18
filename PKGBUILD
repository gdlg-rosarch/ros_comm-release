# Script generated with Bloom
pkgdesc="ROS - rosgraph contains the rosgraph command-line tool, which prints information about the ROS Computation Graph. It also provides an internal library that can be used by graphical tools."
url='http://ros.org/wiki/rosgraph'

pkgname='ros-lunar-rosgraph'
pkgver='1.13.6_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('python2-mock'
'ros-lunar-catkin>=0.5.78'
)

depends=('python2-netifaces'
'python2-rospkg'
'python2-yaml'
)

conflicts=()
replaces=()

_dir=rosgraph
source=()
md5sums=()

prepare() {
    cp -R $startdir/rosgraph $srcdir/rosgraph
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

