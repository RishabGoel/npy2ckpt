#!/usr/bin/env python
import tensorflow as tf
import argparse

# Modify this depending on the graph (.py) generated generated by caffe2tensorflow
from models.net import Net

def convert(model_data_path, output_path='/tmp/model.ckpt'):
    '''Convert the caffe model parameters to .ckpt.'''

    # Set the data specifications for the model
    width = None
    height = None
    channels = None
    input_node_name = None

    assert width and height and channels and input_node_name is not None, \
    'Please, fill the model parameters'

    # Create a placeholder for the input image
    input_node = tf.placeholder(tf.float32,
                                shape=(None, height, width, channels),
                                name='inputs')

    # Construct the network
    net = Net({'input_node_name': input_node})

    with tf.Session() as sesh:
        # Load the converted parameters
        print('Loading the model...')
        net.load(model_data_path, sesh)

        saver = tf.train.Saver()
        save_path = saver.save(sesh, output_path)
        print("\nModel saved in file: %s" % save_path)


def main():
    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('model_path', help='Model parameters (.npy)')
    parser.add_argument('-output_path', help='Model checkpoints (.ckpt)')
    args = parser.parse_args()

    # Convert the model parameters to .ckpt
    if args.output_path:
        convert(args.model_path, output_path)
    else:
        convert(args.model_path)


if __name__ == '__main__':
    main()
