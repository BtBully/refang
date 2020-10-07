# refang
### Script to undo an unknown defanging process applied to IP addresses

Takes a string, containing a transformed IP address, and returns all possible results of reversing the transformation.

 - Original IP address assumed to be four groups of three integers, seperated by periods.

 - Transformation includes inserting an unknown number of characters (numeric and non-numeric) and removing an unknown number of periods.

 - Currently assumes any IP address is valid if it contains four groups of three integers that are equal to, or less than, 255.
