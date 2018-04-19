# Script generated with Bloom
pkgdesc="ROS - Tests for rostopic."
url='http://ros.org/wiki/rostopic'

pkgname='ros-melodic-test-rostopic'
pkgver='1.13.6_3'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-melodic-catkin>=0.5.68'
'ros-melodic-genmsg'
'ros-melodic-genpy'
'ros-melodic-rostest'
'ros-melodic-rostopic'
'ros-melodic-std-msgs'
)

depends=()

conflicts=()
replaces=()

_dir=test_rostopic
source=()
md5sums=()

prepare() {
    cp -R $startdir/test_rostopic $srcdir/test_rostopic
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/melodic/setup.bash ] && source /opt/ros/melodic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/melodic \
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

