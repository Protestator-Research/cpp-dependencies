pipeline {
    agent any
    
    stages {
        stage('clone repo') {
            steps {
                git 'https://github.com/Protestator-Research/cpp-dependencies'
            }
        }
        stage('prep runner') {
            steps {
                sh script: '''conan remove "*" -c'''
            }
        }
        stage('m4') {
            steps {
                sh script: '''conan create ./m4/all --name=m4 --version=1.4.20 --build-require'''
                sh script: '''conan create ./m4/all --name=m4 --version=1.4.20 --build-require -s build_type=Debug --build missing'''
                sh script: '''conan upload "*" -r protestator-conan -c'''
                sh script: '''conan remove "*" -c'''
            }
        }
        stage('cmake') {
            steps {
                sh script: '''conan create ./cmake/binary --name=cmake --version=4.1.2 --build-require'''
                sh script: '''conan create ./cmake/binary --name=cmake --version=4.1.2 --build-require -s build_type=Debug --build missing'''
                sh script: '''conan upload "*" -r protestator-conan -c'''
                sh script: '''conan remove "*" -c'''
            }
        }
        stage('autoconf') {
            steps {
                sh script: '''conan create ./autoconf/all --name=autoconf --version=2.72 --build-require'''
                sh script: '''conan create ./autoconf/all --name=autoconf --version=2.72 --build-require -s build_type=Debug --build missing'''
                sh script: '''conan upload "*" -r protestator-conan -c'''
                sh script: '''conan remove "*" -c'''
            }
        }
        stage('automake') {
            steps {
                sh script: '''conan create ./automake/all --name=automake --version=1.16.5 --build-require'''
                sh script: '''conan create ./automake/all --name=automake --version=1.16.5 --build-require -s build_type=Debug --build missing'''
                sh script: '''conan upload "*" -r protestator-conan -c'''
                sh script: '''conan remove "*" -c'''
            }
        }
        stage('ninja') {
            steps {
                sh script: '''conan create ./ninja/all --name=ninja --version=1.13.1 --build-require'''
                sh script: '''conan create ./ninja/all --name=ninja --version=1.13.1 --build-require -s build_type=Debug --build missing'''
                sh script: '''conan upload "*" -r protestator-conan -c'''
                sh script: '''conan remove "*" -c'''
            }
        }
        stage('meson') {
            steps {
                sh script: '''conan create ./meson/all --name=meson --version=1.9.1 --build-require'''
                sh script: '''conan create ./meson/all --name=meson --version=1.9.1 --build-require -s build_type=Debug --build missing'''
                sh script: '''conan upload "*" -r protestator-conan -c'''
                sh script: '''conan remove "*" -c'''
            }
        }
        stage('pkgconf') {
            steps {
                sh script: '''conan create ./pkgconf/all --name=pkgconf --version=2.5.1 --build-require --build missing'''
                sh script: '''conan create ./pkgconf/all --name=pkgconf --version=2.5.1 --build-require --build missing -s build_type=Debug --build missing'''
                sh script: '''conan upload "*" -r protestator-conan -c'''
                sh script: '''conan remove "*" -c'''
            }
        }
        stage('bison') {
            steps {
                sh script: '''conan create ./bison/all --name=bison --version=3.8.2 --build-require'''
                sh script: '''conan create ./bison/all --name=bison --version=3.8.2 --build-require -s build_type=Debug'''
                sh script: '''conan upload "*" -r protestator-conan -c'''
                sh script: '''conan remove "*" -c'''
            }
        }
        stage('gperf') {
            steps {
                sh script: '''conan create ./gperf/all --name=gperf --version=3.1 --build-require'''
                sh script: '''conan create ./gperf/all --name=gperf --version=3.1 --build-require -s build_type=Debug'''
                sh script: '''conan upload "*" -r protestator-conan -c'''
                sh script: '''conan remove "*" -c'''
            }
        }
        stage('xorg') {
            steps {
                sh script: '''conan create ./xorg/all --name=xorg --version=system --build missing'''
                sh script: '''conan create ./xorg/all --name=xorg --version=system --build missing -s build_type=Debug'''
                sh script: '''conan upload "*" -r protestator-conan -c'''
                sh script: '''conan remove "*" -c'''
            }
        }
        stage('xkeyboard-config') {
            steps {
                sh script: '''conan create ./xkeyboard-config/all --name=xkeyboard-config --version=system'''
                sh script: '''conan create ./xkeyboard-config/all --name=xkeyboard-config --version=system -s build_type=Debug'''
                sh script: '''conan upload "*" -r protestator-conan -c'''
                sh script: '''conan remove "*" -c'''
            }
        }
        stage('gnu-config') {
            steps {
                sh script: '''conan create ./gnu-config/all --name=gnu-config --version=cci.20210814'''
                sh script: '''conan create ./gnu-config/all --name=gnu-config --version=cci.20210814 -s build_type=Debug'''
                sh script: '''conan upload "*" -r protestator-conan -c'''
                sh script: '''conan remove "*" -c'''
            }
        }
        stage('opengl') {
            steps {
                sh script: '''conan create ./opengl/all --name=opengl --version=system'''
                sh script: '''conan create ./opengl/all --name=opengl --version=system -s build_type=Debug'''
                sh script: '''conan upload "*" -r protestator-conan -c'''
                sh script: '''conan remove "*" -c'''
            }
        }
        stage('b2') {
            steps {
                sh script: '''conan create ./b2/portable --name=b2 --version=5.3.3'''
                sh script: '''conan create ./b2/portable --name=b2 --version=5.3.3 -s build_type=Debug'''
                sh script: '''conan upload "*" -r protestator-conan -c'''
                sh script: '''conan remove "*" -c'''
            }
        }
        stage('lz4') {
            steps {
                sh script: '''conan create ./lz4/all --name=lz4 --version=1.9.4'''
                sh script: '''conan create ./lz4/all --name=lz4 --version=1.9.4 -s build_type=Debug'''
                sh script: '''conan upload "*" -r protestator-conan -c'''
                sh script: '''conan remove "*" -c'''
            }
        }
        stage('nasm') {
            steps {
                sh script: '''conan create ./nasm/all --name=nasm --version=2.16.01'''
                sh script: '''conan create ./nasm/all --name=nasm --version=2.16.01 -s build_type=Debug'''
                sh script: '''conan upload "*" -r protestator-conan -c'''
                sh script: '''conan remove "*" -c'''
            }
        }
        stage('linux-headers-generic') {
            steps {
                sh script: '''conan create ./linux-headers-generic/all --name=linux-headers-generic --version=6.5.9'''
                sh script: '''conan create ./linux-headers-generic/all --name=linux-headers-generic --version=6.5.9 -s build_type=Debug'''
                sh script: '''conan upload "*" -r protestator-conan -c'''
                sh script: '''conan remove "*" -c'''
            }
        }
        stage('termcap') {
            steps {
                sh script: '''conan create ./termcap/all --name=termcap --version=1.3.1'''
                sh script: '''conan create ./termcap/all --name=termcap --version=1.3.1 -s build_type=Debug'''
                sh script: '''conan upload "*" -r protestator-conan -c'''
                sh script: '''conan remove "*" -c'''
            }
        }
        stage('antlr-runtime') {
            steps {
                sh script: '''conan create ./antlr4-cppruntime/all --name=antlr4-cppruntime --version=4.13.2'''
                sh script: '''conan create ./antlr4-cppruntime/all --name=antlr4-cppruntime --version=4.13.2 -s build_type=Debug'''
                sh script: '''conan upload "*" -r protestator-conan -c'''
                sh script: '''conan remove "*" -c'''
            }
        }
        stage('zlib') {
            steps {
                sh script: '''conan create ./zlib/all --name=zlib --version=1.3.1'''
                sh script: '''conan create ./zlib/all --name=zlib --version=1.3.1 -s build_type=Debug'''
                sh script: '''conan upload "*" -r protestator-conan -c'''
                sh script: '''conan remove "*" -c'''
            }
        }
        stage('bzip2') {
            steps {
                sh script: '''conan create ./bzip2/all --name=bzip2 --version=1.0.8'''
                sh script: '''conan create ./bzip2/all --name=bzip2 --version=1.0.8 -s build_type=Debug'''
                sh script: '''conan upload "*" -r protestator-conan -c'''
                sh script: '''conan remove "*" -c'''
            }
        }
        stage('brotli') {
            steps {
                sh script: '''conan create ./brotli/all --name=brotli --version=1.1.0'''
                sh script: '''conan create ./brotli/all --name=brotli --version=1.1.0 -s build_type=Debug'''
                sh script: '''conan upload "*" -r protestator-conan -c'''
                sh script: '''conan remove "*" -c'''
            }
        }
        stage('double-conversion') {
            steps {
                sh script: '''conan create ./double-conversion/all --name=double-conversion --version=3.3.0'''
                sh script: '''conan create ./double-conversion/all --name=double-conversion --version=3.3.0 -s build_type=Debug'''
                sh script: '''conan upload "*" -r protestator-conan -c'''
                sh script: '''conan remove "*" -c'''
            }
        }
        stage('expat') {
            steps {
                sh script: '''conan create ./expat/all --name=expat --version=2.7.3'''
                sh script: '''conan create ./expat/all --name=expat --version=2.7.3 -s build_type=Debug'''
                sh script: '''conan upload "*" -r protestator-conan -c'''
                sh script: '''conan remove "*" -c'''
            }
        }
        stage('flex') {
            steps {
                sh script: '''conan create ./flex/all --name=flex --version=2.6.4 --build missing'''
                sh script: '''conan create ./flex/all --name=flex --version=2.6.4 --build missing -s build_type=Debug'''
                sh script: '''conan upload "*" -r protestator-conan -c'''
                sh script: '''conan remove "*" -c'''
            }
        }
        stage('icu') {
            steps {
                sh script: '''conan create ./icu/all --name=icu --version=77.1 --build missing'''
                sh script: '''conan create ./icu/all --name=icu --version=77.1 --build missing -s build_type=Debug'''
                sh script: '''conan upload "*" -r protestator-conan -c'''
                sh script: '''conan remove "*" -c'''
            }
        }
        stage('libbacktrace') {
            steps {
                sh script: '''conan create ./libbacktrace/all --name=libbacktrace --version=cci.20240730'''
                sh script: '''conan create ./libbacktrace/all --name=libbacktrace --version=cci.20240730 -s build_type=Debug'''
                sh script: '''conan upload "*" -r protestator-conan -c'''
                sh script: '''conan remove "*" -c'''
            }
        }
        stage('libelf') {
            steps {
                sh script: '''conan create ./libelf/all --name=libelf --version=0.8.13'''
                sh script: '''conan create ./libelf/all --name=libelf --version=0.8.13 -s build_type=Debug'''
                sh script: '''conan upload "*" -r protestator-conan -c'''
                sh script: '''conan remove "*" -c'''
            }
        }
        stage('libpng') {
            steps {
                sh script: '''conan create ./libpng/all --name=libpng --version=1.6.50'''
                sh script: '''conan create ./libpng/all --name=libpng --version=1.6.50 -s build_type=Debug'''
                sh script: '''conan upload "*" -r protestator-conan -c'''
                sh script: '''conan remove "*" -c'''
            }
        }
        stage('libffi') {
            steps {
                sh script: '''conan create ./libffi/all --name=libffi --version=3.4.8'''
                sh script: '''conan create ./libffi/all --name=libffi --version=3.4.8 -s build_type=Debug'''
                sh script: '''conan upload "*" -r protestator-conan -c'''
                sh script: '''conan remove "*" -c'''
            }
        }
        stage('libiconv') {
            steps {
                sh script: '''conan create ./libiconv/all --name=libiconv --version=1.17'''
                sh script: '''conan create ./libiconv/all --name=libiconv --version=1.17 -s build_type=Debug'''
                sh script: '''conan upload "*" -r protestator-conan -c'''
                sh script: '''conan remove "*" -c'''
            }
        }
        stage('libmount') {
            steps {
                sh script: '''conan create ./libmount/all --name=libmount --version=2.40.2'''
                sh script: '''conan create ./libmount/all --name=libmount --version=2.40.2 -s build_type=Debug'''
                sh script: '''conan upload "*" -r protestator-conan -c'''
                sh script: '''conan remove "*" -c'''
            }
        }
        stage('md4c') {
            steps {
                sh script: '''conan create ./md4c/all --name=md4c --version=0.5.2'''
                sh script: '''conan create ./md4c/all --name=md4c --version=0.5.2 -s build_type=Debug'''
                sh script: '''conan upload "*" -r protestator-conan -c'''
                sh script: '''conan remove "*" -c'''
            }
        }
        stage('nlohmann_json') {
            steps {
                sh script: '''conan create ./nlohmann_json/all --name=nlohmann_json --version=3.11.3'''
                sh script: '''conan create ./nlohmann_json/all --name=nlohmann_json --version=3.11.3 -s build_type=Debug'''
                sh script: '''conan upload "*" -r protestator-conan -c'''
                sh script: '''conan remove "*" -c'''
            }
        }
        stage('sqlite3') {
            steps {
                sh script: '''conan create ./sqlite3/all --name=sqlite3 --version=3.50.4'''
                sh script: '''conan create ./sqlite3/all --name=sqlite3 --version=3.50.4 -s build_type=Debug'''
                sh script: '''conan upload "*" -r protestator-conan -c'''
                sh script: '''conan remove "*" -c'''
            }
        }
        stage('libtool') {
            steps {
                sh script: '''conan create ./libtool/all --name=libtool --version=2.4.7'''
                sh script: '''conan create ./libtool/all --name=libtool --version=2.4.7 -s build_type=Debug'''
                sh script: '''conan upload "*" -r protestator-conan -c'''
                sh script: '''conan remove "*" -c'''
            }
        }
        stage('nspr') {
            steps {
                sh script: '''conan create ./nspr/all --name=nspr --version=4.35'''
                sh script: '''conan create ./nspr/all --name=nspr --version=4.35 -s build_type=Debug'''
                sh script: '''conan upload "*" -r protestator-conan -c'''
                sh script: '''conan remove "*" -c'''
            }
        }
        stage('util-linux-libuuid') {
            steps {
                sh script: '''conan create ./util-linux-libuuid/all --name=util-linux-libuuid --version=2.39.2'''
                sh script: '''conan create ./util-linux-libuuid/all --name=util-linux-libuuid --version=2.39.2 -s build_type=Debug'''
                sh script: '''conan upload "*" -r protestator-conan -c'''
                sh script: '''conan remove "*" -c'''
            }
        }
        stage('pcre2') {
            steps {
                sh script: '''conan create ./pcre2/all --name=pcre2 --version=10.44'''
                sh script: '''conan create ./pcre2/all --name=pcre2 --version=10.44 -s build_type=Debug'''
                sh script: '''conan upload "*" -r protestator-conan -c'''
                sh script: '''conan remove "*" -c'''
            }
        }
        stage('xz_utils') {
            steps {
                sh script: '''conan create ./xz_utils/all --name=xz_utils --version=5.4.5'''
                sh script: '''conan create ./xz_utils/all --name=xz_utils --version=5.4.5 -s build_type=Debug'''
                sh script: '''conan upload "*" -r protestator-conan -c'''
                sh script: '''conan remove "*" -c'''
            }
        }
        stage('gettext') {
            steps {
                sh script: '''conan create ./gettext/all --name=gettext --version=0.22.5'''
                sh script: '''conan create ./gettext/all --name=gettext --version=0.22.5 -s build_type=Debug'''
                sh script: '''conan upload "*" -r protestator-conan -c'''
                sh script: '''conan remove "*" -c'''
            }
        }
        stage('zstd') {
            steps {
                sh script: '''conan create ./zstd/all --name=zstd --version=1.5.7'''
                sh script: '''conan create ./zstd/all --name=zstd --version=1.5.7 -s build_type=Debug'''
                sh script: '''conan upload "*" -r protestator-conan -c'''
                sh script: '''conan remove "*" -c'''
            }
        }
        stage('elfutils') {
            steps {
                sh script: '''conan create ./elfutils/all --name=elfutils --version=0.190'''
                sh script: '''conan create ./elfutils/all --name=elfutils --version=0.190 -s build_type=Debug'''
                sh script: '''conan upload "*" -r protestator-conan -c'''
                sh script: '''conan remove "*" -c'''
            }
        }
        stage('openssl') {
            steps {
                sh script: '''conan create ./openssl/3.x.x --name=openssl --version=3.6.0'''
                sh script: '''conan create ./openssl/3.x.x --name=openssl --version=3.6.0 -s build_type=Debug'''
                sh script: '''conan upload "*" -r protestator-conan -c'''
                sh script: '''conan remove "*" -c'''
            }
        }
        stage('odbc') {
            steps {
                sh script: '''conan create ./odbc/all --name=odbc --version=2.3.11'''
                sh script: '''conan create ./odbc/all --name=odbc --version=2.3.11 -s build_type=Debug'''
                sh script: '''conan upload "*" -r protestator-conan -c'''
                sh script: '''conan remove "*" -c'''
            }
        }
        stage('libxml2') {
            steps {
                sh script: '''conan create ./libxml2/cmake --name=libxml2 --version=2.15.0'''
                sh script: '''conan create ./libxml2/cmake --name=libxml2 --version=2.15.0 -s build_type=Debug'''
                sh script: '''conan upload "*" -r protestator-conan -c'''
                sh script: '''conan remove "*" -c'''
            }
        }
        stage('freetype') {
            steps {
                sh script: '''conan create ./freetype/meson --name=freetype --version=2.14.1'''
                sh script: '''conan create ./freetype/meson --name=freetype --version=2.14.1 -s build_type=Debug'''
                sh script: '''conan upload "*" -r protestator-conan -c'''
                sh script: '''conan remove "*" -c'''
            }
        }
        stage('fontconfig') {
            steps {
                sh script: '''conan create ./fontconfig/all --name=fontconfig --version=2.15.0'''
                sh script: '''conan create ./fontconfig/all --name=fontconfig --version=2.15.0 -s build_type=Debug'''
                sh script: '''conan upload "*" -r protestator-conan -c'''
                sh script: '''conan remove "*" -c'''
            }
        }
        stage('wayland') {
            steps {
                sh script: '''conan create ./wayland/all --name=wayland --version=1.22.0'''
                sh script: '''conan create ./wayland/all --name=wayland --version=1.22.0 -s build_type=Debug'''
                sh script: '''conan upload "*" -r protestator-conan -c'''
                sh script: '''conan remove "*" -c'''
            }
        }
        stage('wayland-protocols') {
            steps {
                sh script: '''conan create ./wayland-protocols/all --name=wayland-protocols --version=1.45 --build-require'''
                sh script: '''conan create ./wayland-protocols/all --name=wayland-protocols --version=1.45 --build-require -s build_type=Debug'''
                sh script: '''conan upload "*" -r protestator-conan -c'''
                sh script: '''conan remove "*" -c'''
            }
        }
        stage('clean runner') {
            steps {
                sh script: '''conan remove "*" -c'''
            }
        }
    }
}