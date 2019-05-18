-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 14, 2019 at 12:26 PM
-- Server version: 10.1.28-MariaDB
-- PHP Version: 7.1.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `mode4`
--

-- --------------------------------------------------------

--
-- Table structure for table `colleges`
--

CREATE TABLE `colleges` (
  `sr_no` int(11) NOT NULL,
  `college` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `colleges`
--

INSERT INTO `colleges` (`sr_no`, `college`) VALUES
(461, ' Gujarat Power Engg. And Research Institute (GPERI)\n'),
(462, ' Kankeshwari Devi Institute of Technology (KIT)\n'),
(463, ' L. J. Institute Of Engineering And Technology (LJIET)\n'),
(464, ' Laxmi Institute of Technology (LIT)	\n'),
(465, ' Shri Labhubhai Trivedi Institute of Engineering And Technology	\n'),
(466, ' Veerayatan Group Of Institutions Faculty Of Engg (VGI)	\n'),
(467, ' AD Patel Institute of Technology (ADPIT)	\n'),
(468, ' Ahmadabad Institute of Technology (AIT)	\n'),
(469, ' Alpha College of Engineering and Technology	\n'),
(470, ' Amiraj College of Engineering And Technology. (ACET)	\n'),
(471, ' Arrdekta Institute of Technology (AIT)	\n'),
(472, ' Arun Muchhala Engineering College (AMEC)	\n'),
(473, ' Atmiya Institute of Technology & Science (AITS)	\n'),
(474, ' B.H. Gardi College of Engineering & Technology (BHGCET)	\n'),
(475, ' BHAGAVAD GOPAL INSTITUTE OF ENGINEERING	\n'),
(476, ' Babaria Instiute of Technology (BIT)	\n'),
(477, ' Bhagwan Mahaveer College of Engineering and Technology (BMCET)	\n'),
(478, ' Birla Vishvakarma Mahavidyalaya Engineering College (BVM)	\n'),
(479, ' Birla Vishwakarma Mahavidyalaya (BVM)	\n'),
(480, ' CEPT University (CEPT)	\n'),
(481, ' CK Pithawala College of Engineering & Technology (CKPET)	\n'),
(482, ' CU Shah College Of Engineering and Technology (CCET)	\n'),
(483, ' Central Institute of Plastic Engineering & Technology (CIPET)	\n'),
(484, ' Chanubhai S Patel Institute of Technology (CSPIT)	\n'),
(485, ' Charotar Institute of Technology	 \n'),
(486, ' Chhotubhai Gopalbhai Patel Institute of Technology (CGPIT)	\n'),
(487, ' DC Patel School of Architecture	\n'),
(488, ' Darshan Institute of Engineering and Technology (DIET)	\n'),
(489, ' Dharamsingh Desai Institute of Technology	\n'),
(490, ' Dr. Jivraj Mehta Institute of Technology (DJMIT)	\n'),
(491, ' Engineering College Tuwa (ECT)	\n'),
(492, ' Faculty Of Technology and Engineering, M.S.Univ Of Baroda (FTE-MSU)	\n'),
(493, ' Faculty of Engineering, Techonology & Research (FETR),	\n'),
(494, ' GH Patel College of Engineering & Technology (GCET)	\n'),
(495, ' GK Bharad Institute of Engineering	\n'),
(496, ' GUJARAT INSTITUTE OF TECHNICAL STUDIES (GITS)	\n'),
(497, ' Gandhinagar Institute of Technology (GIT)	\n'),
(498, ' Gidc Degree Engineering College. (GDEC)	\n'),
(499, ' Government Engineering College	\n'),
(500, ' Government Engineering College (Bastar)	\n'),
(501, ' Government Engineering College (Bastar)	\n'),
(502, ' Government Engineering College (Bhavnagar)	\n'),
(503, ' Government Engineering College (Gandhi Nagar)	\n'),
(504, ' Government Engineering College Bharuch (GECB)	\n'),
(505, ' Government Engineering College Bhuj (GEC-BHUJ)	\n'),
(506, ' Government Engineering College Dahod (GEC-DAHOD)	\n'),
(507, ' Government Engineering College Gandhinagar (GECG)	\n'),
(508, ' Government Engineering College Godhra (GECG)	\n'),
(509, ' Government Engineering College Modasa (GEC-MODASA)\n'),
(510, ' Government Engineering College Patan (GECP)	\n'),
(511, ' Government Engineering College Surat (GEC-SURAT)	\n'),
(512, ' Government Engineering College Valsad (GECV)	\n'),
(513, ' Government Engineering College(GEC, Rajkot)	\n'),
(514, ' HJD Institute of Technical Education and Research (HITER)	\n'),
(515, ' Hansaba College of Engineering and Technology (HCET)	\n'),
(516, ' Hasmukh Goswami College of Engineering (HGCE)	\n'),
(517, ' Indus Institute of Engineering & Technology (IITE)	\n'),
(518, ' Indus Institute of Technology & Engineering (IITE)	\n'),
(519, ' Institute of Computer and Communication Technology (ICCT)	\n'),
(520, ' Institute of Science and Technology for Advanced Studies and Research (ISTAR)\n'),
(521, ' Institute of Technology & Management Universe Technical Campus (ITMU)	\n'),
(522, ' Ipcowala Institute of Engineering & Technology (IIET)	\n'),
(523, ' K.J Institute of Engineering and Technology (KJIT)	\n'),
(524, ' Kalol Institute of Technology & Researach Centre (KITRC)\n'),
(525, ' LC Institute of Technology (LCIT)	\n'),
(526, ' LD College of Engineering (LDCE)	\n'),
(527, ' Lakhu Pole Near Kotharia Village	\n'),
(528, ' Leads Institute of Technology & Engineering (LITE)	\n'),
(529, ' Leelaben Dashrathbhai Ramdas Patel Institute of Technology and Research (LDRP-ITR)	\n'),
(530, ' Lukhdhirji College of Engineering (LCE)	\n'),
(531, ' Lukhdhirji Engineering College (LEC)	\n'),
(532, ' Mahatma Gandhi Institute of Technology Education & Residence Centre (MGITERC)	\n'),
(533, ' Marwadi Education Foundation Group of Institutions (MEFGI)	\n'),
(534, ' Merchant Engineering College Basna (MEC)	\n'),
(535, ' Narnarayan Shastri Institute Of Technology (NSIT)	\n'),
(536, ' Nirma Institute of Technology	\n'),
(537, ' Noble Engineering College (NEC)	\n'),
(538, ' Noble Group of Institutions (NGI)\n'),
(539, ' Om Shanti Engineering College (OSEC)	\n'),
(540, ' Pacific School of Engineering (PSE)	\n'),
(541, ' Parul Institute of Engineering & Technology (PIET)	\n'),
(542, ' Parul Institute of Technology (PIT)	\n'),
(543, ' RK College of Engineering & Technology (RKCET)	\n'),
(544, ' Rungta College of Engineering & Technology	\n'),
(545, ' SAL Institute of Technology and Engineering Research (SALITER)	\n'),
(546, ' SHRI SATSANGI SAKETDHAM RAM ASHRAM GROUP OF INSTITUTIONS (SSSRAI)	\n'),
(547, ' SPB Patel Engineering College (SPEC)\n'),
(548, ' SV National Institute of Technology	\n'),
(549, ' Sabar Institute of Technology For Girls (SITG)	\n'),
(550, ' Samarth College of Engineering and Technology (SCET)	\n'),
(551, ' Sankalchand Patel College of Engineering (SPCE)\n'),
(552, ' Sardar Patel Institute of Technology (SPIT)	\n'),
(553, ' Sardar Vallabhbhai Patel Institute of Technology (SVIT)	\n'),
(554, ' Sarvajanik College of Engineering & Technology (SCET)	\n'),
(555, ' Shankersinh Vaghela Bapu Institute of Technology (SVBIT)	\n'),
(556, ' Shantilal Shah Engineering College (SSEC)	\n'),
(557, ' Shree Swami Atmanand Saraswati Institute of Technology ( SSASIT)	\n'),
(558, ' Shri. J. M. Sabva Insitute of Engineering & Technology (JMSIET)	\n'),
(559, ' Shroff Sr Rotary Institute of Chemical Technology (SRICT)	\n'),
(560, ' Sigma Institute of Engineering (SIE)	\n'),
(561, ' Sigma Institute of Technology and Engineering	\n'),
(562, ' Silver Oak College Of Engineering and Technology (SOCET)	\n'),
(563, ' Smt. S.R. Patel Engineering College (SRPEC)	\n'),
(564, ' Takshashila College of Engineering and Technology (TCET)	\n'),
(565, ' Tatva Institute of Technological Studies (TITS)	\n'),
(566, ' U V Patel College of Engineering (UVPCE)	\n'),
(567, ' Universal College of Engineering and Technology (UCET)	\n'),
(568, ' V. V. P Engineering College (VVPEC)	\n'),
(569, ' Vadodara Institute of Engineering (VIE)	\n'),
(570, ' Valia Institute of Technology (VIT)	\n'),
(571, ' Venus International College of Technology (VICT)	\n'),
(572, ' Vidhyadeep Institute of Management & Technology (VIMT)	\n'),
(573, ' Vidyabharti Trust Institute of Technology and Research Center (VBTITRC)	\n'),
(574, ' Vishwakarma Government Engineering College, Chandkheda (VGEC)\n'),
(575, ' Vyavsai Vidya Prathisthans Sanch College of Engineering (VVP)	\n');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `colleges`
--
ALTER TABLE `colleges`
  ADD PRIMARY KEY (`sr_no`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `colleges`
--
ALTER TABLE `colleges`
  MODIFY `sr_no` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=576;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
