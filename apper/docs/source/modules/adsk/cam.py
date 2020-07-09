# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  cam.py
#
#  This file is a component of ApperSample.
#
#  Copyright (c) 2020 by Patrick Rainsberry.
#  :license: Apache2, see LICENSE for more details.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  cam.py
#
#  This file is a component of ApperSample.
#
#  Copyright (c) 2020 by Patrick Rainsberry.
#  :license: Apache2, see LICENSE for more details.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# This file is automatically generated for code intellisense only.
# It does not reflect the actual implementation.

from . import core
from . import fusion


class CAM(core.Product):
    """
    Object that represents the CAM environment of a Fusion document.
    """

    def __init__(self):
        super().__init__()

    @staticmethod
    def cast(arg):
        return CAM()

    def _get_setups(self):
        return Setups()

    def _get_allOperations(self):
        return core.ObjectCollection()

    def _get_genericPostFolder(self):
        return str()

    def _get_personalPostFolder(self):
        return str()

    def _get_temporaryFolder(self):
        return str()

    def _get_customGraphicsGroups(self):
        return fusion.CustomGraphicsGroups()

    def _get_designRootOccurrence(self):
        return fusion.Occurrence()

    def _get_flatPatternOccurrences(self):
        return fusion.OccurrenceList()

    def export3MFForDefaultAdditiveSetup(self):
        return bool()

    def generateToolpath(self, operations):
        """
        Generates/Regenerates all of the toolpaths (including those nested in sub-folders or patterns) for the
        specified objects. operations : An Operation, Setup, Folder or Pattern object for which to generate the
        toolpath/s for. You can also specify a collection of any combination of these object types. Return
        GenerateToolpathFuture that includes the status of toolpath generation.
        """
        return GenerateToolpathFuture()

    def generateAllToolpaths(self, skipValid):
        """
        Generates/Regenerates all toolpaths (includes those nested in sub-folders or patterns) in the document.
        skipValid : Option to skip valid toolpaths and only regenerate invalid toolpaths.
        Return GenerateToolpathFuture that includes the status of toolpath generation.
        """
        return GenerateToolpathFuture()

    def clearToolpath(self, operations):
        """
        Clears all of the toolpaths (including those nested in sub-folders or patterns) for the specified objects.
        operations : An Operation, Setup, Folder or Pattern object for which to clear the toolpath/s for. You can
        also specify a collection of any combination of these object types. Return true if successful.
        """
        return bool()

    def clearAllToolpaths(self):
        """
        Clears all the toolpaths (includes those nested in sub-folders or patterns) in the document
        Return true if successful.
        """
        return bool()

    def checkToolpath(self, operations):
        """
        Checks if toolpath operations (including those nested in sub-folders or patterns) are valid for the specified
        objects. operations : An Operation, Setup, Folder or Pattern object for which to check the toolpath/s of. You
        can also specify a collection of any combination of these object types. Returns true if the toolpath
        operations are valid
        """
        return bool()

    def checkAllToolpaths(self):
        """
        Checks if all the toolpath operations (includes those nested in sub-folders or patterns) in the document are
        valid Returns true if the all toolpath operations are valid
        """
        return bool()

    def postProcess(self, operations, input):
        """
        Post all of the toolpaths (including those nested in sub-folders or patterns) for the specified objects
        operations : An Operation, Setup, Folder or Pattern object for which to post the toolpath/s of. You can also
        specify a collection of any combination of these object types. input : The PostProcessInput object that
        defines the post options and parameters. Returns true if successful
        """
        return bool()

    def postProcessAll(self, input):
        """
        Post all of the toolpaths (includes those nested in sub-folders or patterns)in the document
        input : The PostProcessInput object that defines the post options and parameters.
        Returns true if successful
        """
        return bool()

    def generateSetupSheet(self, operations, format, folder, openDocument):
        """
        Generate the setup sheets for the specified objects operations : An Operation, Setup, Folder or Pattern
        object for which to generate the setup sheet/s for. You can also specify a collection of any combination of
        these object types. format : The document format for the setup sheet. Valid options are HTMLFormat and
        ExcelFormat. Limitation: 'ExcelFormat' can be used in windows OS only. folder : The destination folder to
        locate the setup sheet documents in. openDocument : An option to allow to open the document instantly after
        the generation. By default, the document is opened. Returns true if successful
        """
        return bool()

    def generateAllSetupSheets(self, format, folder, openDocument):
        """
        Generates all of the setup sheets for all of the operations in the document format : The document format for
        the setup sheet. Valid options are HTMLFormat and ExcelFormat. Limitation: 'ExcelFormat' can be used in
        windows OS only. folder : The destination folder to locate the setup sheet documents in. openDocument : An
        option to allow to open the document instantly after the generation. By default, the document is opened.
        Returns true if successful
        """
        return bool()

    def getMachiningTime(self, operations, feedScale, rapidFeed, toolChangeTime):
        """
        Get the machining time for the specified objects. operations : An Operation, Setup, Folder or Pattern object
        for which to get the machining time for. You can also specify a collection of any combination of these object
        types. feedScale : The feed scale value (%) to use. rapidFeed : The rapid feed rate in centimeters per
        second. toolChangeTime : The tool change time in seconds. Returns a MachiningTime object that has properties
        holding the calculation results.
        """
        return MachiningTime()

    setups = property(_get_setups, None, doc="Returns the Setups collection that provides access to existing setups")
    allOperations = property(_get_allOperations, None,
                             doc="Gets a collection containing all of the operations in the document. This includes "
                                 "all operations nested in folders and patterns.")
    genericPostFolder = property(_get_genericPostFolder, None, doc="Gets the installation folder with the posts.")
    personalPostFolder = property(_get_personalPostFolder, None, doc="Gets the personal post folder.")
    temporaryFolder = property(_get_temporaryFolder, None, doc="Gets the folder for temporary files.")
    customGraphicsGroups = property(_get_customGraphicsGroups, None,
                                    doc="Returns the customGraphicsGroups object associated with the CAM product.")
    designRootOccurrence = property(_get_designRootOccurrence, None,
                                    doc="Returns the occurrence that references the design root component in CAM "
                                        "product.")
    flatPatternOccurrences = property(_get_flatPatternOccurrences, None,
                                      doc="Returns a read only list of flat pattern occurrences in CAM product.")


class CAMFolders(core.Base):
    """
    Collection that provides access to the folders within an existing setup, folder or pattern.
    """

    def __init__(self):
        super().__init__()

    @staticmethod
    def cast(arg):
        return CAMFolders()

    def _get_count(self):
        return int()

    def item(self, index):
        """
        Function that returns the specified folder using an index into the collection. index : The index of the item
        within the collection to return. The first item in the collection has an index of 0. Returns the specified
        item or null if an invalid index was specified.
        """
        return CAMFolder()

    def itemByName(self, name):
        """
        Returns the folder of the specified name (as appears in the browser).
        name : The name (as it appears in the browser) of the folder.
        Returns the specified folder or null in the case where there is no folder with the specified name.
        """
        return CAMFolder()

    count = property(_get_count, None, doc="The number of items in the collection.")


class CAMPatterns(core.Base):
    """
    Collection that provides access to the patterns within an existing setup, folder or pattern.
    """

    def __init__(self):
        super().__init__()

    @staticmethod
    def cast(arg):
        return CAMPatterns()

    def _get_count(self):
        return int()

    def item(self, index):
        """
        Function that returns the specified pattern using an index into the collection. index : The index of the item
        within the collection to return. The first item in the collection has an index of 0. Returns the specified
        item or null if an invalid index was specified.
        """
        return CAMPattern()

    def itemByName(self, name):
        """
        Returns the pattern of the specified name (as appears in the browser).
        name : The name (as it appears in the browser) of the pattern.
        Returns the specified pattern or null in the case where there is no pattern with the specified name.
        """
        return CAMPattern()

    count = property(_get_count, None, doc="The number of items in the collection.")


class ChildOperationList(core.Base):
    """
    Provides access to the collection of child operations, folders and patterns of an existing setup.
    """

    def __init__(self):
        super().__init__()

    @staticmethod
    def cast(arg):
        return ChildOperationList()

    def _get_count(self):
        return int()

    def item(self, index):
        """
        Returns the specified item using an index into the collection. index : The index of the item within the
        collection to return. The first item in the collection has an index of 0. Returns the specified item or null
        if an invalid index was specified.
        """
        return core.Base()

    def itemByName(self, name):
        """
        Returns the operation, folder or pattern of the specified name (the name seen in the browser).
        name : The name of the operation, folder or pattern as seen in the browser.
        Returns the specified item or null in the case where there is no item with the specified name.
        """
        return core.Base()

    count = property(_get_count, None, doc="Gets the number of objects in the collection.")


class GenerateToolpathFuture(core.Base):
    """
    Used to check the state and get back the results of toolpath generation.
    """

    def __init__(self):
        super().__init__()

    @staticmethod
    def cast(arg):
        return GenerateToolpathFuture()

    def _get_numberOfOperations(self):
        return int()

    def _get_numberOfCompleted(self):
        return int()

    def _get_operations(self):
        return Operations()

    def _get_isGenerationCompleted(self):
        return bool()

    numberOfOperations = property(_get_numberOfOperations, None,
                                  doc="Returns a number of operations need to be generated.")
    numberOfCompleted = property(_get_numberOfCompleted, None,
                                 doc="Returns a number of operations whose toolpath generation are completed.")
    operations = property(_get_operations, None, doc="Returns all operations that need to be generated.")
    isGenerationCompleted = property(_get_isGenerationCompleted, None,
                                     doc="Returns true if all operations are generated.")


class MachiningTime(core.Base):
    """
    Object returned when using the getMachiningTime method from the CAM class. Use the properties on this object to
    get the machining time results.
    """

    def __init__(self):
        super().__init__()

    @staticmethod
    def cast(arg):
        return MachiningTime()

    def _get_feedDistance(self):
        return float()

    def _get_totalFeedTime(self):
        return float()

    def _get_rapidDistance(self):
        return float()

    def _get_totalRapidTime(self):
        return float()

    def _get_toolChangeCount(self):
        return int()

    def _get_totalToolChangeTime(self):
        return float()

    def _get_machiningTime(self):
        return float()

    feedDistance = property(_get_feedDistance, None, doc="Gets the feed distance in centimeters.")
    totalFeedTime = property(_get_totalFeedTime, None, doc="Get the total feed time in seconds.")
    rapidDistance = property(_get_rapidDistance, None, doc="Gets the calculated rapid distance in centimeters.")
    totalRapidTime = property(_get_totalRapidTime, None, doc="Gets the total rapid feed time in seconds.")
    toolChangeCount = property(_get_toolChangeCount, None, doc="Gets the number of tool changes.")
    totalToolChangeTime = property(_get_totalToolChangeTime, None, doc="Gets the total tool change time in seconds.")
    machiningTime = property(_get_machiningTime, None, doc="Gets the machining time in seconds.")


class OperationBase(core.Base):
    """
    Base class object representing all operations, folders, patterns and setups.
    """

    def __init__(self):
        super().__init__()

    @staticmethod
    def cast(arg):
        return OperationBase()

    def _set_name(self, name):
        pass

    def _get_name(self):
        return str()

    def _set_isProtected(self, isProtected):
        pass

    def _get_isProtected(self):
        return bool()

    def _set_isOptional(self, isOptional):
        pass

    def _get_isOptional(self):
        return bool()

    def _set_isSuppressed(self, isSuppressed):
        pass

    def _get_isSuppressed(self):
        return bool()

    def _get_parentSetup(self):
        return Setup()

    name = property(_get_name, _set_name,
                    doc="Gets and sets the name of the operation as seen in the browser. This name is unique as "
                        "compared to the names of all other operations in the document.")
    isProtected = property(_get_isProtected, _set_isProtected,
                           doc="Gets and sets the 'protected' property value of the operation. Gets/sets true if the "
                               "operation is protected.")
    isOptional = property(_get_isOptional, _set_isOptional,
                          doc="Gets and sets the 'Optional' property value of the operation. Gets/sets true if the "
                              "operation is optional.")
    isSuppressed = property(_get_isSuppressed, _set_isSuppressed,
                            doc="Gets and sets the 'Suppressed' property value of the operation. Gets/sets true if "
                                "the operation is suppressed.")
    parentSetup = property(_get_parentSetup, None, doc="Gets the Setup this operation belongs to.")


class Operations(core.Base):
    """
    Collection that provides access to the individual operations within an existing setup, folder or pattern.
    """

    def __init__(self):
        super().__init__()

    @staticmethod
    def cast(arg):
        return Operations()

    def _get_count(self):
        return int()

    def item(self, index):
        """
        Function that returns the specified operation using an index into the collection. index : The index of the
        item within the collection to return. The first item in the collection has an index of 0. Returns the
        specified item or null if an invalid index was specified.
        """
        return Operation()

    def itemByName(self, name):
        """
        Returns the operation of the specified name (as appears in the browser).
        name : The name (as it appears in the browser) of the operation.
        Returns the specified operation or null in the case where there is no operation with the specified name.
        """
        return Operation()

    count = property(_get_count, None, doc="The number of items in the collection.")


class OperationStates:
    """
    The possible states of an operation
    """

    def __init__(self):
        pass

    IsValidOperationState = 0
    IsInvalidOperationState = 1
    SuppressedOperationState = 2
    NoToolpathOperationState = 3


class OperationStrategyTypes:
    """
    The valid options for the Strategy Type of an operation.
    """

    def __init__(self):
        pass

    AdaptiveClearing2D = 0
    Pocket2D = 1
    Face = 2
    Contour2D = 3
    Slot = 4
    Trace = 5
    Thread = 6
    Bore = 7
    Circular = 8
    Engrave = 9
    AdaptiveClearing = 10
    PocketClearing = 11
    Parallel = 12
    Contour = 13
    Ramp = 14
    Horizontal = 15
    Pencil = 16
    Scallop = 17
    Spiral = 18
    Radial = 19
    MorphedSpiral = 20
    Projection = 21
    Drilling = 22
    Jet2D = 23
    TurningChamfer = 24
    TurningFace = 25
    TurningGroove = 26
    TurningPart = 27
    TurningProfile = 28
    TurningProfileGroove = 29
    TurningStockTransfer = 30
    TurningThread = 31


class OperationTypes:
    """
    The valid options for the Operation Type of a Setup.
    """

    def __init__(self):
        pass

    MillingOperation = 0
    TurningOperation = 1
    JetOperation = 2


class PostOutputUnitOptions:
    """
    List of the valid options for the outputUnit property on a PostProcessInput object .
    """

    def __init__(self):
        pass

    DocumentUnitsOutput = 0
    InchesOutput = 1
    MillimetersOutput = 2


class PostProcessInput(core.Base):
    """
    This class defines the properties that pertain to the settings and options required for posting a toolpath to
    generate a CNC file. A PostProcessInput object is a required parameter for the postProcessAll() and postProcess()
    methods on the CAM class.
    """

    def __init__(self):
        super().__init__()

    @staticmethod
    def cast(arg):
        """

        :param arg:
        :return:
        """
        return PostProcessInput()

    @staticmethod
    def create(programName, postConfiguration, outputFolder, outputUnits):
        """
        Creates a new PostProcessInput object to be used as an input arguement by the postProcess() and
        postProcessAll() methods on the CAM class for posting toolpaths and generating CNC files. programName : The
        program name or number. If the post configuration specifies the parameter programNameIsInteger = true,
        then the program name must be a number. postConfiguration : The full filename (including the path) for the
        post configuration file (.cps) The post config file can be stored in any path but for convenience you can use
        the genericPostFolder or the personalPostFolder property on the CAM class to specify the path if your .cps
        file is stored in either of those locations. You must add a forward slash (this works for Mac or Windows) to
        the path defined by these folder properties before the filename (i.e. postConfiguration =
        cam.genericPostFolder + '/' + 'fanuc.cps') outputFolder : The path for the existing output folder where the
        .cnc files will be located. This method will create the specified output folder if it does not already exist.
        It is not necessary to add a slash to the end of the outputFolder path. You should use forward slashes in
        your path definition if you want your script to run on both Mac and Windows. outputUnits : The units option
        for the cnc output. Valid options are DocumentUnitsOutput, InchesOutput or MillimetersOutput Returns the
        newly created PostProcessInput object or null if the creation failed.
        """
        return PostProcessInput()

    def _set_programName(self, programName):
        pass

    def _get_programName(self):
        return str()

    def _set_programComment(self, programComment):
        pass

    def _get_programComment(self):
        return str()

    def _set_postConfiguration(self, postConfiguration):
        pass

    def _get_postConfiguration(self):
        return str()

    def _set_outputFolder(self, outputFolder):
        pass

    def _get_outputFolder(self):
        return str()

    def _set_outputUnits(self, outputUnits):
        pass

    def _get_outputUnits(self):
        return PostOutputUnitOptions()

    def _set_isOpenInEditor(self, isOpenInEditor):
        pass

    def _get_isOpenInEditor(self):
        return bool()

    def _set_areToolChangesMinimized(self, areToolChangesMinimized):
        pass

    def _get_areToolChangesMinimized(self):
        return bool()

    programName = property(_get_programName, _set_programName,
                           doc="Gets and sets the program name or number. If the post configuration specifies the "
                               "parameter programNameIsInteger = true, then the program name must be a number.")
    programComment = property(_get_programComment, _set_programComment,
                              doc="Gets and sets the program comment. The default value for this property is an empty "
                                  "string ('').")
    postConfiguration = property(_get_postConfiguration, _set_postConfiguration,
                                 doc="Gets and sets the full filename (including the path) for the post configuration "
                                     "file (.cps)")
    outputFolder = property(_get_outputFolder, _set_outputFolder,
                            doc="Gets and sets the path for the output folder where the .cnc files will be located.")
    outputUnits = property(_get_outputUnits, _set_outputUnits,
                           doc="Gets and sets the units option for the cnc output. Valid options are "
                               "DocumentUnitsOutput, InchesOutput or MillimetersOutput")
    isOpenInEditor = property(_get_isOpenInEditor, _set_isOpenInEditor,
                              doc="Gets and sets the option if opening the cnc file with the editor after it is "
                                  "created. The default value for this property is true.")
    areToolChangesMinimized = property(_get_areToolChangesMinimized, _set_areToolChangesMinimized,
                                       doc="Gets and sets that operations may be reordered between setups to minimize "
                                           "the number of tool changes. Operations within each setup will still be "
                                           "executed in the programmed order. This is commonly used for tombstone "
                                           "machining where you have multiple setups. The default value for this "
                                           "property is false.")


class Setups(core.Base):
    """
    Collection that provides access to all of the existing setups in a document.
    """

    def __init__(self):
        super().__init__()

    @staticmethod
    def cast(arg):
        return Setups()

    def _get_count(self):
        return int()

    def item(self, index):
        """
        Function that returns the specified setup using an index into the collection. index : The index of the item
        within the collection to return. The first item in the collection has an index of 0. Returns the specified
        item or null if an invalid index was specified.
        """
        return Setup()

    def itemByName(self, name):
        """
        Returns the setup of the specified name.
        name : The name (as it appears in the browser) of the operation.
        Returns the specified setup or null in the case where there is no setup with the specified name.
        """
        return Setup()

    count = property(_get_count, None, doc="The number of setups in the collection.")


class SetupSheetFormats:
    """
    List of the formats to choose from when generating setup sheets
    """

    def __init__(self):
        pass

    HTMLFormat = 0
    ExcelFormat = 1


class CAMFolder(OperationBase):
    """
    Object that represents a folder in an existing Setup, Folder or Pattern.
    """

    def __init__(self):
        super().__init__()

    @staticmethod
    def cast(arg):
        return CAMFolder()

    def _get_isActive(self):
        return bool()

    def _get_operations(self):
        return Operations()

    def _get_folders(self):
        return CAMFolders()

    def _get_patterns(self):
        return CAMPatterns()

    def _get_children(self):
        return ChildOperationList()

    def _get_parent(self):
        return core.Base()

    def _get_allOperations(self):
        return core.ObjectCollection()

    isActive = property(_get_isActive, None, doc="Gets if this folder is active.")
    operations = property(_get_operations, None,
                          doc="Returns the Operations collection that provides access to existing individual "
                              "operations in this folder.")
    folders = property(_get_folders, None,
                       doc="Returns the Folders collection that provides access to existing folders in this folder.")
    patterns = property(_get_patterns, None,
                        doc="Returns the Patterns collection that provides access to existing patterns in this folder.")
    children = property(_get_children, None,
                        doc="Returns a collection containing all of the immediate (top level) child operations, "
                            "folders and patterns in this folder in the order they appear in the browser.")
    parent = property(_get_parent, None, doc="Returns the parent Setup, Folder or Pattern for this Folder.")
    allOperations = property(_get_allOperations, None,
                             doc="Gets a collection containing all of the operations in this folder. This includes "
                                 "all operations nested in folders and patterns.")


class Operation(OperationBase):
    """
    Object that represents an operation in an existing Setup, Folder or Pattern.
    """

    def __init__(self):
        super().__init__()

    @staticmethod
    def cast(arg):
        return Operation()

    def _get_strategyType(self):
        return OperationStrategyTypes()

    def _get_isToolpathValid(self):
        return bool()

    def _get_isGenerating(self):
        return bool()

    def _get_hasWarning(self):
        return bool()

    def _get_parent(self):
        return core.Base()

    def _get_hasToolpath(self):
        return bool()

    def _get_operationState(self):
        return OperationStates()

    def _get_generatingProgress(self):
        return str()

    strategyType = property(_get_strategyType, None, doc="Gets the strategy type for this operation.")
    isToolpathValid = property(_get_isToolpathValid, None,
                               doc="Gets if the toolpath for this operation is currently valid. (has not become "
                                   "invalidated by model changes).")
    isGenerating = property(_get_isGenerating, None, doc="Gets if the toolpath is in the process of generating.")
    hasWarning = property(_get_hasWarning, None,
                          doc="Gets if problems were encountered when generating the toolpath for this operation.")
    parent = property(_get_parent, None, doc="Returns the parent Setup, Folder or Pattern for this operation.")
    hasToolpath = property(_get_hasToolpath, None,
                           doc="Gets if a toolpath currently exists (has been generated) for this operation.")
    operationState = property(_get_operationState, None, doc="Gets the current state of this operation.")
    generatingProgress = property(_get_generatingProgress, None,
                                  doc="Gets the toolpath generation progress value for this operation.")


class Setup(OperationBase):
    """
    Object that represents an existing Setup.
    """

    def __init__(self):
        super().__init__()

    @staticmethod
    def cast(arg):
        return Setup()

    def _get_operationType(self):
        return OperationTypes()

    def _get_isActive(self):
        return bool()

    def _get_operations(self):
        return Operations()

    def _get_folders(self):
        return CAMFolders()

    def _get_patterns(self):
        return CAMPatterns()

    def _get_children(self):
        return ChildOperationList()

    def _get_allOperations(self):
        return core.ObjectCollection()

    def _set_models(self, models):
        pass

    def _get_models(self):
        return core.ObjectCollection()

    operationType = property(_get_operationType, None,
                             doc="Gets the Operation Type (MillingOperation or TurningOperation).")
    isActive = property(_get_isActive, None, doc="Gets if this setup is active.")
    operations = property(_get_operations, None,
                          doc="Returns the Operations collection that provides access to existing operations in this "
                              "setup.")
    folders = property(_get_folders, None,
                       doc="Returns the Folders collection that provides access to existing folders in this setup.")
    patterns = property(_get_patterns, None,
                        doc="Returns the Patterns collection that provides access to existing patterns in this setup.")
    children = property(_get_children, None,
                        doc="Returns a collection containing all of the immediate (top level) child operations, "
                            "folders and patterns in this setup in the order they appear in the browser.")
    allOperations = property(_get_allOperations, None,
                             doc="Gets a collection containing all of the operations in this setup. This includes all "
                                 "operations nested in folders and patterns.")
    models = property(_get_models, _set_models,
                      doc="Gets and sets the bodies associated with the setup. Passing in an empty ObjectCollection "
                          "will remove all current bodies. Valid input is MeshBody and/or BRepBody objects.")


class CAMPattern(CAMFolder):
    """
    Object that represents a pattern in an existing Setup, Folder or Pattern.
    """

    def __init__(self):
        super().__init__()

    @staticmethod
    def cast(arg):
        return CAMPattern()
