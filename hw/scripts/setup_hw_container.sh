cd /

wget https://apache.jfrog.io/artifactory/arrow/$(lsb_release --id --short | tr 'A-Z' 'a-z')/apache-arrow-apt-source-latest-$(lsb_release --codename --short).deb
sudo apt install -y ./apache-arrow-apt-source-latest-$(lsb_release --codename --short).deb
rm ./apache-arrow-apt-source-latest-$(lsb_release --codename --short).deb

sudo apt-get update
sudo apt-get upgrade

sudo apt-get install -y git cmake build-essential ca-certificates lsb-release wget

sudo apt-get install -y libnetcdf-dev

sudo apt-get install -y libarrow-dev
sudo apt-get install -y libarrow-glib-dev
sudo apt-get install -y libarrow-dataset-dev
sudo apt-get install -y libarrow-dataset-glib-dev
sudo apt-get install -y libarrow-acero-dev
sudo apt-get install -y libarrow-flight-dev
sudo apt-get install -y libarrow-flight-glib-dev
sudo apt-get install -y libarrow-flight-sql-dev
sudo apt-get install -y libarrow-flight-sql-glib-dev
sudo apt-get install -y libgandiva-dev
sudo apt-get install -y libgandiva-glib-dev
sudo apt-get install -y libparquet-dev
sudo apt-get install -y libparquet-glib-dev

git clone https://github.com/google/flatbuffers.git
cd flatbuffers
cmake -G "Unix Makefiles" -DCMAKE_BUILD_TYPE=Release
make
sudo make install
cd ../
rm -rf flatbuffers

git clone -b v1.1.3 https://github.com/duckdb/duckdb.git
cd duckdb
make
cp build/release/src/libduckdb.so /workspace/SemanticDataService/third_party_lib/duckdb/lib/
cp src/include/duckdb.h /workspace/SemanticDataService/third_party_lib/duckdb/include/
cp src/include/duckdb.hpp /workspace/SemanticDataService/third_party_lib/duckdb/include/
cp -R src/include/duckdb /workspace/SemanticDataService/third_party_lib/duckdb/include/
cd ../
rm -rf duckdb
