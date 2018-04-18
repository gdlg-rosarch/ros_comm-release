# Script generated with Bloom
pkgdesc="ROS - Tools for directing, throttling, selecting, and otherwise messing with ROS topics at a meta level. None of the programs in this package actually know about the topics whose streams they are altering; instead, these tools deal with messages as generic binary blobs. This means they can be applied to any ROS topic."
url='http://ros.org/wiki/topic_tools'

pkgname='ros-kinetic-topic-tools'
pkgver='1.12.13_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin>=0.5.78'
'ros-kinetic-cpp-common'
'ros-kinetic-message-generation'
'ros-kinetic-rosconsole'
'ros-kinetic-roscpp'
'ros-kinetic-rostest'
'ros-kinetic-rostime'
'ros-kinetic-rosunit'
'ros-kinetic-std-msgs'
'ros-kinetic-xmlrpcpp'
)

depends=('ros-kinetic-message-runtime'
'ros-kinetic-rosconsole'
'ros-kinetic-roscpp'
'ros-kinetic-rostime'
'ros-kinetic-std-msgs'
'ros-kinetic-xmlrpcpp'
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
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
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

