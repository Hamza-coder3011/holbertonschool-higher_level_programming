#!/usr/bin/node
const arg = ProcessingInstruction.argv[2];
if (arg === undefined){
	console.log('No argument');
} else {
	console.log(arg);
}