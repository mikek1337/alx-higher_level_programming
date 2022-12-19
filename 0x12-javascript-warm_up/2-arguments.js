#!/usr/bin/node
import { argv } from 'node::process';

if (argv.length > 0) {
  console.log('Argument found');
} else { console.log('No argument'); }
