# Positron oddities

I have no idea why, but when building packages with Positron, I get the error:

"WARNING: ignoring environment value of R_HOME\n/usr/share/R/"

Further research suggests that this is something to do with R_HOME and R_HOME_DIR differing
(may be Arch Linus specific)

editing the relevant lines of 
/usr/bin/R
to get rid of this warning message seems to fix this, though this is not a permanent solution