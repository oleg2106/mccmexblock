"""TO-DO: Write a description of what this XBlock is."""

import pkg_resources

from xblock.core import XBlock
from xblock.fields import Scope, String, Integer, Float, Boolean
from xblock.fragment import Fragment

import re
from xml.etree import ElementTree as ET

class MccmeXBlock(XBlock):
    """
    TO-DO: document what your XBlock does.
    """

    # Fields are defined on the class.  You can access them in your code as
    # self.<fieldname>.

    # TO-DO: delete count, and define your own fields.
    answer = Float(
        values={"min": 0},
        default=None, scope=Scope.user_state,
        help="User answer",
    )
    state = String(
        default=None, scope=Scope.user_state,
        help="State of block",
    )

    href = String(
        display_name="IFrame src",
        help=("IFrame url"),
        default='',
        scope=Scope.settings
    )

    width = String(
        display_name="IFrame width",
        help=("IFrame width"),
        default='100%',
        scope=Scope.settings
    )

    height = String(
        display_name="IFrame Height",
        help=("IFrame Height"),
        default='500px',
        scope=Scope.settings
    )

    

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    def studio_view(self, context=None):
        """
        Create a fragment used to display the edit view in the Studio.
        """
        html = self.resource_string("static/html/mccmexblock_edit.html")
        frag = Fragment(html.format(self=self))
        frag.add_javascript(self.resource_string("static/js/src/mccmexblock_edit.js"))
        frag.initialize_js('MccmeXBlockEditBlock')
        
        return frag

    @XBlock.json_handler
    def studio_submit(self, data, suffix=''):
        """
        Called when submitting the form in Studio.
        """
        self.href = data.get('href')
        self.width  = data.get('width')
        self.height = data.get('height')

        return {'result': 'success'}

    #def edit_view(self, context=None):
        #text = self.resource_string("static/html/mccmexblock.xml")
        #p = re.compile('<mccme_problem>.+</mccme_problem>', re.S)
        #problem = p.search(text)
        #if problem:
            #xmltext = problem.group()
            #try:
                #x = ET.fromstring(xmltext)
   
                #for t in x.findall('customresponse'):
                    #width  = t.find('width').text
                    #height = t.find('height').text
                    #iframe = t.find('iframe').text
            #except:
                #pass
            
        #frag = Fragment(html.format(self=self))
        #return frag


    # TO-DO: change this view to display your data your own way.
    def student_view(self, context=None):
        """
        The primary view of the MccmeXBlock, shown to students
        when viewing courses.
        """
        #if not self.href:
            #self.href = 'http://localhost/html/xmodule_example2/example_form.html'
        
        html = self.resource_string("static/html/mccmexblock.html")
        frag = Fragment(html.format(self=self))
        frag.add_javascript_url(self.runtime.local_resource_url(self, 'public/js/jschannel.js'))
        frag.add_javascript(self.resource_string("static/js/src/mccmexblock.js"))
        frag.initialize_js('MccmeXBlock', {'state': self.state,
                                           'answer': self.answer})
        return frag

    # TO-DO: change this handler to perform your own actions.  You may need more
    # than one handler, or you may not need any handlers at all.
    @XBlock.json_handler
    def save_answer(self, data, suffix=''):
        self.answer = float(data['value']);

    @XBlock.json_handler
    def save_state(self, data, suffix=''):
        # save it in string format. Dont need to unpack it
        self.state = data['value']

    # TO-DO: change this to create the scenarios you'd like to see in the
    # workbench while developing your XBlock.
    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("MccmeXBlock",
             """<mccmexblock/>
             """),
            ("Multiple MccmeXBlock",
             """<vertical_demo>
                <mccmexblock/>
                </vertical_demo>
             """),
        ]
