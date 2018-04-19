# Script generated with Bloom
pkgdesc="ROS - Tests for roscpp which depend on rostest."
url='http://ros.org/wiki/roscpp'

pkgname='ros-melodic-test-roscpp'
pkgver='1.13.6_3'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('pkg-config'
'ros-melodic-catkin>=0.5.68'
'ros-melodic-cpp-common'
'ros-melodic-message-generation'
'ros-melodic-rosconsole'
'ros-melodic-roscpp'
'ros-melodic-roscpp-serialization'
'ros-melodic-roscpp-traits'
'ros-melodic-rosgraph-msgs'
'ros-melodic-roslang'
'ros-melodic-rostest'
'ros-melodic-rostime'
'ros-melodic-rosunit'
'ros-melodic-std-msgs'
'ros-melodic-std-srvs'
'ros-melodic-xmlrpcpp'
)

depends=('ros-melodic-message-runtime'
'ros-melodic-rosconsole'
'ros-melodic-rosgraph-msgs'
'ros-melodic-std-msgs'
'ros-melodic-std-srvs'
'ros-melodic-xmlrpcpp'
)

conflicts=()
replaces=()

_dir=test_roscpp
source=()
md5sums=()

prepare() {
    cp -R $startdir/test_roscpp $srcdir/test_roscpp
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

