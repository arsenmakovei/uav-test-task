import argparse

from dronekit import connect, LocationGlobalRelative

from utils import arm_and_takeoff, condition_yaw


parser = argparse.ArgumentParser(
    description="Commands vehicle using vehicle.simple_goto."
)
parser.add_argument(
    "--connect",
    help="Vehicle connection target string. If not specified, SITL automatically started and used.",
)
args = parser.parse_args()

connection_string = args.connect
sitl = None

# Start SITL if no connection string specified
if not connection_string:
    import dronekit_sitl

    sitl = dronekit_sitl.start_default()
    connection_string = sitl.connection_string()

# Connect to the Vehicle
print("Connecting to vehicle on: %s" % connection_string)
vehicle = connect(connection_string, wait_ready=True)

arm_and_takeoff(vehicle, 100)

print("Set default/target airspeed to 3")
vehicle.airspeed = 3

print("Going towards first point for 30 seconds ...")
point1 = LocationGlobalRelative(50.450739, 30.461242, 100)
vehicle.simple_goto(point1)

print("Going towards second point for 30 seconds (groundspeed set to 10 m/s) ...")
point2 = LocationGlobalRelative(50.443326, 30.448078, 100)
vehicle.simple_goto(point2, groundspeed=10)

print("Set absolute yaw angle to 350 degrees")
condition_yaw(vehicle, 350)

# Close vehicle object before exiting script
print("Close vehicle object")
vehicle.close()

# Shut down simulator if it was started.
if sitl:
    sitl.stop()
