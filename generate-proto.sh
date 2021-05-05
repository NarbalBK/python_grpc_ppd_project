#!/bin/bash
echo "Generating proto grpc files..."
python -m grpc_tools.protoc -I=./ --python_out=./ --grpc_python_out=./ ./helloworld.proto
echo "DONE"
