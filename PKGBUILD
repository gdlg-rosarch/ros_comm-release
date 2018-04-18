# Script generated with Bloom
pkgdesc="ROS - rosmsg contains two command-line tools: <tt>rosmsg</tt> and <tt>rossrv</tt>. <tt>rosmsg</tt> is a command-line tool for displaying information about <a href="http://www.ros.org/wiki/msg">ROS Message types</a>. <tt>rossrv</tt> is a command-line tool for displaying information about <a href="http://www.ros.org/wiki/srv">ROS Service types</a>."
url='http://ros.org/wiki/rosmsg'

pkgname='ros-lunar-rosmsg'
pkgver='1.13.6_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-lunar-catkin'
'ros-lunar-std-msgs'
)

depends=('python2-rospkg'
'ros-lunar-catkin>=0.6.4'
'ros-lunar-genmsg'
'ros-lunar-genpy>=0.6.5'
'ros-lunar-rosbag'
'ros-lunar-roslib'
)

conflicts=()
replaces=()

_dir=rosmsg
source=()
md5sums=()

prepare() {
    cp -R $startdir/rosmsg $srcdir/rosmsg
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

