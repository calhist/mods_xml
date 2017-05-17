<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xmlns:xs="http://www.w3.org/2001/XMLSchema">

	<xsl:output method="xml" version="1.0" encoding="UTF-8" indent="yes" media-type="text/xml"/>

	<xsl:variable name="braces">[]</xsl:variable>
	<xsl:variable name="no_braces"></xsl:variable>

	<xsl:template match="/">
		<mods xmlns="http://www.loc.gov/mods/v3" xmlns:mods="http://www.loc.gov/mods/v3" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xlink="http://www.w3.org/1999/xlink" xsi:schemaLocation="http://www.loc.gov/mods/v3 http://www.loc.gov/mods/v3/mods-3-5.xsd">

			<titleInfo>
				<title>
					<xsl:variable name="titlefix" select="translate(mods:mods/mods:titleInfo/mods:title, $braces, $no_braces)"/>
					<xsl:value-of select="$titlefix"/>
				</title>
			</titleInfo>

			<xsl:copy>
				<xsl:apply-templates select="mods:mods/mods:identifier"/>
			</xsl:copy>

			<name type="personal" authority="naf">
				<namePart>Wagner, Anton</namePart>
				<role>
					<roleTerm type="text">Creator</roleTerm>
				</role>
			</name>

			<xsl:copy>
				<xsl:apply-templates select="mods:mods/mods:genre"/>
			</xsl:copy>
			<genre authority="gmgpc">Photographs</genre>

			<xsl:for-each select="mods:mods/mods:note">
				<xsl:if test="mods:mods/mods:note[not(@preferredCitation)]">
					<xsl:copy>
						<xsl:apply-templates select="mods:mods/mods:note"/>
					</xsl:copy>
				</xsl:if>
			</xsl:for-each>

			<note type="preferredCitation">
				<xsl:variable name="titlefix" select="translate(mods:mods/mods:titleInfo/mods:title, $braces, $no_braces)"/>
				<xsl:value-of select="$titlefix"/>
				<xsl:text>, Los Angeles: 1932-33, PC 017, California Historical Society</xsl:text>
			</note>
			<note type="general">Title supplied by cataloger.</note>

			<originInfo>
				<dateCreated encoding="w3cdtf" keyDate="yes">
					<xsl:value-of select="mods:mods/mods:originInfo/mods:dateCreated"/>
				</dateCreated>
			</originInfo>

			<accessCondition type="useAndReproduction">All requests to reproduce, publish, quote from or otherwise use collection materials must be submitted in writing to the Director of Library and Archives. Consent is given on behalf of the California Historical Society as the owner of the physical items and is not intended to include or imply permission from the copyright owner. Such permission must be obtained from the copyright owner. Restrictions also apply to digital representations of the original materials. Use of digital files is restricted to research and educational purposes. Responsibility for any use, including copying, transmitting, or making any other use of protected images, rests exclusively with the user. Upon request, digitized works can be removed from public view if there are rights issues that need to be resolved.</accessCondition>
			<accessCondition type="useAndReproduction" xlink:href="http://rightsstatements.org/vocab/NKC/1.0/">No Known Copyright</accessCondition>

			<xsl:if test="//mods:coordinates[text()!=',']">
				<subject>
					<cartographics>
						<coordinates>
								<xsl:value-of select="//mods:coordinates"/>
						</coordinates>
					</cartographics>
				</subject>
			</xsl:if>

			<xsl:for-each select="//mods:topic[@authority='local']">
				<subject authority="local">
					<topic>
						<xsl:value-of select="."/>
					</topic>
				</subject>
			</xsl:for-each>

			<xsl:for-each select="//mods:topic[@authority='lcsh']">
				<subject authority="lcsh">
					<xsl:if test="text()='Streets--California--Los Angeles County--Photographs'">
						<topic>Streets</topic>
					</xsl:if>

					<!-- do more stuff here! -->

				</subject>
			</xsl:for-each>

			<subject authority="lcsh">
				<geographic>Los Angeles (Calif.)</geographic>
			</subject>

			<relatedItem type="host">
				<titleInfo>
					<title>Los Angeles: 1932-33</title>
				</titleInfo>
				<identifier type="local">PC 017</identifier>
				<location>
					<physicalLocation>California Historical Society</physicalLocation>
				</location>
			</relatedItem>
			<typeOfResource>still image</typeOfResource>
		</mods>
	</xsl:template>

	<xsl:strip-space elements="*"/>
	<xsl:template match="*[not(node())]"/>    
	<xsl:template match="node()|@*">
	    <xsl:copy>
	        <xsl:apply-templates select="node()[normalize-space()]|@*[normalize-space()]"/>
	    </xsl:copy>
	</xsl:template>

</xsl:stylesheet>