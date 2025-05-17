# Databricks notebook source
storageAccountName = "blobdemoplatform"
storageAccountAccessKey = ""
sasToken = ""

blobContainerName = "streamramanpls"
mountPoint = "/mnt/datalakehouse/"
if any(mount.mountPoint == mountPoint for mount in dbutils.fs.mounts()):
    dbutils.fs.unmount(mountPoint)
try:
    dbutils.fs.mount(
        source="wasbs://{}@{}.blob.core.windows.net".format(
            blobContainerName, storageAccountName
        ),
        mount_point=mountPoint,
        # extra_configs = {'fs.azure.account.key.' + storageAccountName + '.blob.core.windows.net': storageAccountAccessKey}
        extra_configs={
            "fs.azure.sas."
            + blobContainerName
            + "."
            + storageAccountName
            + ".blob.core.windows.net": sasToken
        },
    )
    print("mount succeeded!")
except Exception as e:
    print("mount exception", e)
