class AadharNotseededError(Exception):
    pass

is_aadhar_seeded = False

if(is_aadhar_seeded == False):
    raise AadharNotseededError("Aadhar is not seeded")