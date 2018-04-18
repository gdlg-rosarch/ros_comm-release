# Script generated with Bloom
pkgdesc="ROS - Tools for directing, throttling, selecting, and otherwise messing with ROS topics at a meta level. None of the programs in this package actually know about the topics whose streams they are altering; instead, these tools deal with messages as generic binary blobs. This means they can be applied to any ROS topic."
url='http://ros.org/wiki/topic_tools'

pkgname='ros-lunar-topic-tools'
pkgver='1.13.6_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-lunar-catkin>=0.5.78'
'ros-lunar-cpp-common'
'ros-lunar-message-generation'
'ros-lunar-rosconsole'
'ros-lunar-roscpp'
'ros-lunar-rostest'
'ros-lunar-rostime'
'ros-lunar-rosunit'
'ros-lunar-std-msgs'
'ros-lunar-xmlrpcpp'
)

depends=('ros-lunar-message-runtime'
'ros-lunar-rosconsole'
'ros-lunar-roscpp'
'ros-lunar-rostime'
'ros-lunar-std-msgs'
'ros-lunar-xmlrpcpp'
)

conflicts=()
replaces=()

_dir=topic_tools
source=()
md5sums=()

prepare() {
    cp -R $startdir/topic_tools $srcdir/topic_tools
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

